import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate, FewShotChatMessagePromptTemplate
from sympy.physics.units import temperature

#os.environ['OPENAI_API_KEY'] = ''
os.environ['GOOGLE_API_KEY'] = ''


def createPromptTemplate(message):
    return ChatPromptTemplate.from_messages(message)


if __name__ == '__main__':

    example_prompt = createPromptTemplate(
        [
            ("human", "{input}"),
            ("ai", "{output}")
        ]
    )

    examples = [
        {
            "input": "지구의 대기 중 가장 많은 비율을 차지하는 기체는 무엇인가요?",
            "output": "지구 대기의 약 78%를 차지하는 질소입니다."
        },
        {
            "input": "광합성에 필요한 주요 요소들은 무엇인가요?",
            "output": "광합성에 필요한 주요 요소는 빛, 이산화탄소, 물입니다."
        },
        {
            "input": "피타고라스 정리를 설명해주세요.",
            "output": "피타고라스 정리는 직각삼각형에서 빗변의 제곱이 다른 두 변의 제곱의 합과 같다는 것입니다."
        },
        {
            "input": "지구의 자전 주기는 얼마인가요?",
            "output": "지구의 자전 주기는 약 24시간(정확히는 23시간 56분 4초)입니다."
        },
        {
            "input": "DNA의 기본 구조를 간단히 설명해주세요.",
            "output": "DNA는 두 개의 폴리뉴클레오티드 사슬이 이중 나선 구조를 이루고 있습니다."
        },
        {
            "input": "원주율(π)의 정의는 무엇인가요?",
            "output": "원주율(π)은 원의 지름에 대한 원의 둘레의 비율입니다."
        }
    ]

    few_shot_prompt = FewShotChatMessagePromptTemplate(
        examples=examples,
        example_prompt=example_prompt
    )

    final_prompt = createPromptTemplate(
        [
            ("system", "당신은 과학과 수학에 대해 잘 아는 교육자입니다."),
            few_shot_prompt,
            ("human", "{input}")
        ]
    )

    model = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0, max_output_tokens=200)
    chain = final_prompt | model

    result = chain.invoke({"input": "지구의 자전 주기는 얼마인가요?"})
    print(result.content)
import os
from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI

os.environ['GOOGLE_API_KEY'] = ''

if __name__ == '__main__':
    chat_prompt = ChatPromptTemplate.from_messages(
        [
            ("system", "이 시스템은 여행 전문가입니다."),
            ("user", "{user_input}"),
        ]
    )

    chat_model = ChatGoogleGenerativeAI(
        model="gemini-1.5-flash",
        temperature=0,
        max_output_tokens=200
    )

    chain = chat_prompt | chat_model

    print(chain.invoke({"user_input": "안녕하세요? 한국의 대표적인 관광지 3군대를 추천해주세요."}))
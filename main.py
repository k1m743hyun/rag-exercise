import os

from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI

os.environ['GOOGLE_API_KEY'] = ''

if __name__ == '__main__':
    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", "이 시스템은 천문학 질문에 답변할 수 있습니다."),
            ("user", "{user_input}"),
        ]
    )

    model = ChatGoogleGenerativeAI(model="gemini-1.5-flash", max_tokens=100)

    messages = prompt.format_messages(user_input="태양계에서 가장 큰 행성은 무엇인가요?")

    before_answer = model.invoke(messages)
    print(before_answer)

    chain = prompt | model.bind(max_tokens=10)

    after_answer = chain.invoke({"user_input": "태양계에서 가장 큰 행성은 무엇인가요?"})
    print(after_answer)
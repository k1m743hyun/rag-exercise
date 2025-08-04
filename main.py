import os
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

os.environ['OPENAI_API_KEY'] = ''


def createPrompt(command):
    return ChatPromptTemplate.from_template(command)


if __name__ == '__main__':
    model = ChatOpenAI(model="gpt-4o-mini")
    prompt = createPrompt("지구과학에서 {topic}에 대해 간단히 설명해주세요.")
    output_parser = StrOutputParser()

    chain = prompt | model | output_parser

    #result = chain.invoke({"topic": "지구 자전"})
    #print("invoke 결과:", result)

    topics = ["지구 공전", "화산 활동", "대륙 이동"]
    results = chain.batch([{"topic": topic} for topic in topics])
    for topic, result in zip(topics, results):
        print(f"{topic} 설명: {result[:50]}...")
import os
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

os.environ['OPENAI_API_KEY'] = ''


def createPrompt():
    return ChatPromptTemplate.from_template(
        "You are an expert in astronomy. Answer the question. <Question>: {input}"
    )


if __name__ == '__main__':
    llm = ChatOpenAI(model="gpt-4o-mini")

    #print(llm.invoke("지구의 자전 주기는?"))

    chain = createPrompt() | llm | StrOutputParser()

    print(chain.invoke({"input": "지구의 자전 주기는?"}))
import os
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

os.environ['OPENAI_API_KEY'] = ''


def createPrompt(command):
    return ChatPromptTemplate.from_template(command)


if __name__ == '__main__':
    llm = ChatOpenAI(model="gpt-4o-mini")

    prompt1 = createPrompt("translates {korean_word} to English")
    prompt2 = createPrompt("explain {english_word} using oxford dictionary to me in Korean")

    chain = prompt1 | llm | StrOutputParser()

    print(chain.invoke({"korean_word": "미래"}))
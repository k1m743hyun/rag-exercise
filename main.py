import os
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, SystemMessagePromptTemplate, HumanMessagePromptTemplate
from langchain_core.output_parsers import StrOutputParser

os.environ['OPENAI_API_KEY'] = ''


def createPrompt():
    return ChatPromptTemplate.from_messages([
        SystemMessagePromptTemplate.from_template("이 시스템은 천문학 질문에 답변할 수 있습니다."),
        HumanMessagePromptTemplate.from_template("{user_input}")
    ])


if __name__ == '__main__':
    chat_prompt = createPrompt()

    #messages = chat_prompt.format_messages(user_input="태양계에서 가장 큰 행성은 무엇인가요?")
    #print(messages)

    llm = ChatOpenAI(model="gpt-4o-mini")
    chain = chat_prompt | llm | StrOutputParser()
    print(chain.invoke({"user_input": "태양계에서 가장 큰 행성은 무엇인가요?"}))
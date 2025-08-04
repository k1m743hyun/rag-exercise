import os
from langchain_openai import ChatOpenAI

os.environ['OPENAI_API_KEY'] = ''

if __name__ == '__main__':
    llm = ChatOpenAI(model="gpt-4o-mini")

    print(llm.invoke("지구의 자전 주기는?"))
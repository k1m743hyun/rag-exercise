import os

from click import prompt
from langchain_community.vectorstores import Chroma
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from langchain_community.document_loaders import WebBaseLoader
from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from sympy.physics.units import temperature

os.environ['GOOGLE_API_KEY'] = ''


def format_docs(docs):
    return '\n\n'.join(doc.page_content for doc in docs)

if __name__ == '__main__':
    url = 'https://ko.wikipedia.org/wiki/%EC%9C%84%ED%82%A4%EB%B0%B1%EA%B3%BC:%EC%A0%95%EC%B1%85%EA%B3%BC_%EC%A7%80%EC%B9%A8'
    loader = WebBaseLoader(url)

    docs = loader.load()

    #print(len(docs))
    #print(len(docs[0].page_content))
    #print(docs[0].page_content[5000:6000])

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    splits = text_splitter.split_documents(docs)

    #print(len(splits))
    #print(splits[10])
    #print(splits[10].page_content)
    #print(splits[10].metadata)

    vectorstore = Chroma.from_documents(documents=splits, embedding=GoogleGenerativeAIEmbeddings(model="models/embedding-001"))

    docs = vectorstore.similarity_search("격하 과정에 대해서 설명해주세요.")
    #print(len(docs))
    #print(docs[0].page_content)

    template = '''Answer the question based only on the following context:
    {context}

    Question: {question}
    '''

    prompt = ChatPromptTemplate.from_template(template)

    model = ChatGoogleGenerativeAI(model='gemini-1.5-flash', temperature=0)

    retriever = vectorstore.as_retriever()

    rag_chain = (
        {'context': retriever | format_docs, 'question': RunnablePassthrough()}
        | prompt
        | model
        | StrOutputParser()
    )

    print(rag_chain.invoke("격하 과정에 대해서 설명해주세요."))
import os
from langchain_core.documents import Document
from langchain_community.vectorstores import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings

os.environ['GOOGLE_API_KEY'] = ''

if __name__ == '__main__':
    documents = [
        Document(
            page_content="LangChain은 대규모 언어 모델(LLM)을 사용하는 애플리케이션을 개발하기 위한 프레임워크입니다.",
            metadata={
                "title": "LangChain 소개",
                "author": "AI 개발자",
                "url": "http://example.com/langchain-intro"
            }
        ),
        Document(
            page_content="벡터 데이터베이스는 고차원 벡터를 효율적으로 저장하고 검색하는 데 특화된 데이터베이스 시스템입니다.",
            metadata={
                "title": "벡터 데이터베이스 개요",
                "author": "데이터 과학자",
                "url": "http://example.com/vector-db-overview"
            }
        ),
    ]

    embedding_model = GoogleGenerativeAIEmbeddings(model='models/embedding-001')

    vectorstore = Chroma.from_documents(
        documents,
        embedding_model,
        collection_name='esg',
        persist_directory='./db/chromadb',
    )

    query = 'LangChain이란 무엇인가요?'
    results = vectorstore.similarity_search(query, k=2)

    for doc in results:
        print(f"내용: {doc.page_content}")
        print(f"제목: {doc.metadata['title']}")
        print(f"저자: {doc.metadata['author']}")
        print(f"URL: {doc.metadata['url']}")
        print("---")

import os
from numpy import dot
from numpy.linalg import norm
from langchain_community.vectorstores import Chroma
from langchain_community.document_loaders import PyMuPDFLoader
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter

os.environ['GOOGLE_API_KEY'] = ''

if __name__ == '__main__':
    loader = PyMuPDFLoader('data/323410_카카오뱅크_2023.pdf')
    data = loader.load()

    text_splitter = RecursiveCharacterTextSplitter.from_tiktoken_encoder(
        chunk_size=1000,
        chunk_overlap=200,
        encoding_name='cl100k_base'
    )

    documents = text_splitter.split_documents(data)
    #print(len(documents))

    embedding_model = GoogleGenerativeAIEmbeddings(model='models/embedding-001')

    db = Chroma.from_documents(
        documents,
        embedding_model,
        collection_name='esg',
        persist_directory='./db/chromadb',
        collection_metadata={'hnsw:space': 'cosine'},
    )
    #print(db)

    query = '카카오뱅크의 환경목표와 세부추진내용을 알려줘?'
    docs = db.similarity_search(query)
    #print(len(docs))
    #print(docs[0].page_content)
    #print(docs[-1].page_content)

    mmr_docs =db.max_marginal_relevance_search(query, k=4, fetch_k=10)
    #print(len(mmr_docs))
    #print(mmr_docs[0].page_content)
    print(mmr_docs[-1].page_content)

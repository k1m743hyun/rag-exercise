from langchain_community.document_loaders import PyMuPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.vectorstores.utils import DistanceStrategy

if __name__ == '__main__':
    loader = PyMuPDFLoader('data/323410_카카오뱅크_2023.pdf')
    data = loader.load()

    text_splitter = RecursiveCharacterTextSplitter.from_tiktoken_encoder(
        chunk_size=1000,
        chunk_overlap=200,
        encoding_name='cl100k_base'
    )

    documents = text_splitter.split_documents(data)

    embedding_model = HuggingFaceEmbeddings(
        model_name='jhgan/ko-sbert-nli',
        model_kwargs={'device': 'cpu'},
        encode_kwargs={'normalize_embeddings': True},
    )

    vectorstore = FAISS.from_documents(
        documents,
        embedding_model,
        distance_strategy=DistanceStrategy.COSINE,
    )
    #print(vectorstore)
    #print(vectorstore.distance_strategy)

    query = '카카오뱅크가 중대성 평가를 통해 도출한 6가지 중대 주제는 무엇인가?'
    docs = vectorstore.similarity_search(query)
    print(len(docs))
    print(docs[0].page_content)

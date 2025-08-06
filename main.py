import os
from numpy import dot
from numpy.linalg import norm
from langchain_community.vectorstores import Chroma
from langchain_community.document_loaders import TextLoader
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter

os.environ['GOOGLE_API_KEY'] = ''

def cos_sim(A, B):
    return dot(A, B) / (norm(A) * norm(B))

if __name__ == '__main__':
    loader = TextLoader('data/history.txt')
    data = loader.load()

    text_splitter = RecursiveCharacterTextSplitter.from_tiktoken_encoder(
        chunk_size=250,
        chunk_overlap=50,
        encoding_name='cl100k_base'
    )

    texts = text_splitter.split_text(data[0].page_content)
    #print(texts[0])

    embedding_model = GoogleGenerativeAIEmbeddings(model='models/embedding-001')

    db = Chroma.from_texts(
        texts,
        embedding_model,
        collection_name='history',
        persist_directory='./db/chromadb',
        collection_metadata={'hnsw:space': 'cosine'},
    )
    #print(db)

    query = '누가 한글을 창제했나요?'
    docs = db.similarity_search(query)
    print(docs[0].page_content)

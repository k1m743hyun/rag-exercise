from langchain_community.document_loaders import WebBaseLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

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
    print(splits[10].metadata)

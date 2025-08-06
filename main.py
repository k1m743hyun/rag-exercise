from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import CharacterTextSplitter

if __name__ == '__main__':
    loader = TextLoader('./data/history.txt')
    data = loader.load()
    #print(len(data[0].page_content))
    #print(data[0].page_content)

    text_splitter = CharacterTextSplitter.from_tiktoken_encoder(
        chunk_size=600,
        chunk_overlap=200,
        encoding_name='cl100k_base',
    )

    docs = text_splitter.split_text(data[0].page_content)
    print(len(docs))

    for i in range(len(docs)):
        print(len(docs[i]))
        print(docs[i])

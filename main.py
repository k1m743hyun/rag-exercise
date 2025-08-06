from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import CharacterTextSplitter

if __name__ == '__main__':
    loader = TextLoader('./data/history.txt')
    data = loader.load()
    #print(len(data[0].page_content))
    #print(data[0].page_content)

    text_splitter = CharacterTextSplitter(
        separator='\n',
        chunk_size=500,
        chunk_overlap=100,
        length_function=len,
    )

    texts = text_splitter.split_text(data[0].page_content)
    print(len(texts))
    print(len(texts[0]), len(texts[1]), len(texts[2]))
    print(texts[0])

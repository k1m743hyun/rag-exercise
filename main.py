from langchain_community.document_loaders import TextLoader

if __name__ == '__main__':
    loader = TextLoader('history.txt')
    data = loader.load()

    print(type(data))
    print(len(data))
    print(data)
    print(len(data[0].page_content))
    print(data[0].metadata)
from langchain_community.document_loaders import PyPDFDirectoryLoader

if __name__ == '__main__':
    loader = PyPDFDirectoryLoader('./data')
    data = loader.load()
    print(len(data))
    print(data[0])
    print(data[-1])
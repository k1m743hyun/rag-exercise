from langchain_community.document_loaders import OnlinePDFLoader

if __name__ == '__main__':
    url = 'https://arxiv.org/pdf/1706.03762.pdf'
    loader = OnlinePDFLoader(url)
    pages = loader.load()
    print(len(pages))
    print(pages[0].page_content[:1000])
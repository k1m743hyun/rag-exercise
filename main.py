from langchain_community.document_loaders import PyPDFLoader

if __name__ == '__main__':
    pdf_filepath = './data/000660_SK_2023.pdf'
    loader = PyPDFLoader(pdf_filepath)
    pages = loader.load()
    print(len(pages))
    print(pages[10])
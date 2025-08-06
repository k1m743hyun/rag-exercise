from langchain_community.document_loaders import PyMuPDFLoader

if __name__ == '__main__':
    pdf_filepath = 'data/000660_SK_2023.pdf'
    loader = PyMuPDFLoader(pdf_filepath)
    pages = loader.load()
    print(len(pages))
    print(pages[0].page_content)
    print(pages[0].metadata)
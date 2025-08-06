from langchain_community.document_loaders import UnstructuredPDFLoader

if __name__ == '__main__':
    pdf_filepath = 'data/000660_SK_2023.pdf'
    loader = UnstructuredPDFLoader(pdf_filepath, mode='elements')
    pages = loader.load()
    print(len(pages))
    print(pages[100])
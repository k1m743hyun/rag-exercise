from langchain_community.document_loaders.csv_loader import CSVLoader

if __name__ == '__main__':
    loader = CSVLoader(file_path='./data/한국주택금융공사_주택금융관련_지수_20160101.csv', encoding='cp949')
    data = loader.load()
    print(len(data))
    print(data[0])
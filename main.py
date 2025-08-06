import os
from glob import glob
from langchain_community.document_loaders import TextLoader, DirectoryLoader

if __name__ == '__main__':
    files = glob(os.path.join('./', '*.txt'))
    #print(files)

    loader = DirectoryLoader(path='./', glob='*.txt', loader_cls=TextLoader)
    data = loader.load()
    print(len(data))
    print(data[0])
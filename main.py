import os
from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from langchain_chroma import Chroma
from langchain_core.prompts import PromptTemplate
from langchain_core.example_selectors import SemanticSimilarityExampleSelector
from openai import embeddings

#os.environ['OPENAI_API_KEY'] = ''
os.environ['GOOGLE_API_KEY'] = ''


def createPromptTemplate(message):
    return PromptTemplate.from_template(message)


if __name__ == '__main__':
    prompt = createPromptTemplate("지구의 {layer}에서 가장 흔한 원소는 {element}입니다.")

    partial_prompt = prompt.partial(layer="지각")

    print(partial_prompt.format(element="산소"))
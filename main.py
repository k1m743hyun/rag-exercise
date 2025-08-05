import os
from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from langchain_chroma import Chroma
from langchain_core.prompts import PromptTemplate
from langchain_core.example_selectors import SemanticSimilarityExampleSelector
from openai import embeddings
from datetime import datetime

#os.environ['OPENAI_API_KEY'] = ''
os.environ['GOOGLE_API_KEY'] = ''

def get_current_season():
    month = datetime.now().month
    if 3 <= month <= 5:
        return "봄"
    elif 6 <= month <= 8:
        return "여름"
    elif 9 <= month <= 11:
        return "가을"
    else:
        return "겨울"

def createPromptTemplate(message):
    return PromptTemplate.from_template(message)

if __name__ == '__main__':
    prompt = PromptTemplate(
        template="{season}에 일어나는 대표적인 지구과학 현상은 {phenomenon}입니다.",
        input_variables=["phenomenon"],
        partial_variables={"season": get_current_season}
    )

    print(prompt.format(phenomenon="꽃가루 증가"))
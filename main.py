import os
from langchain_google_genai import GoogleGenerativeAI

#os.environ['OPENAI_API_KEY'] = ''
os.environ['GOOGLE_API_KEY'] = ''

if __name__ == '__main__':
    llm = GoogleGenerativeAI(
        model="gemini-1.5-flash",
        temperature=0,
        max_output_tokens=200
    )

    print(llm.invoke("한국의 대표적인 관광지 3군대를 추천해주세요."))
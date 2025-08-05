import os
from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI

os.environ['GOOGLE_API_KEY'] = ''

if __name__ == '__main__':
    params = {
        "temperature": 0.7,
        "max_tokens": 100
    }

    kwargs = {
        "frequency_penalty": 0.5,
        "presence_penalty": 0.5,
        "stop": ["\n"]
    }

    model = ChatGoogleGenerativeAI(
        model="gemini-1.5-flash",
        **params,
        model_kwargs=kwargs
    )

    question = "태양계에서 가장 큰 행성은 무엇인가요?"
    #print(model.invoke(input=question))

    new_params = {
        "temperature": 0.7,
        "max_tokens": 10,
    }

    print(model.invoke(input=question, **new_params))
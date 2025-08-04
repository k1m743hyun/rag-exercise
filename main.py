import os
import asyncio
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

os.environ['OPENAI_API_KEY'] = ''


def createPrompt(command):
    return ChatPromptTemplate.from_template(command)


if __name__ == '__main__':
    template_text = "안녕하세요, 제 이름은 {name}이고, 나이는 {age}살 입니다."

    prompt_template = createPrompt(template_text)

    filled_prompt = prompt_template.format(name="홍길동", age=30)

    print(filled_prompt)
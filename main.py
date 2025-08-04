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

    combined_prompt = (
        prompt_template
        + createPrompt("\n\n아버지를 아버지라 부를 수 없습니다.")
        + "\n\n{language}로 번역해주세요."
    )

    filled_prompt = combined_prompt.format(name="홍길동", age=30, language="영어")

    print(filled_prompt)
import os
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.pydantic_v1 import BaseModel, Field

os.environ['GOOGLE_API_KEY'] = ''

class CusineRecipe(BaseModel):
    name: str = Field(description="name of a cusine")
    recipe: str = Field(description="recipe to cook the cusine")

if __name__ == '__main__':
    output_parser = JsonOutputParser(pydantic_object=CusineRecipe)
    format_instructions = output_parser.get_format_instructions()
    print(format_instructions)

    prompt = PromptTemplate(
        template="Answer the user query.\n{format_instructions}\n{query}\n",
        input_variables=["query"],
        partial_variables={"format_instructions": format_instructions},
    )
    print(prompt)

    model = ChatGoogleGenerativeAI(
        model="gemini-1.5-flash",
        temperature=0,
        max_tokens=200,
    )

    chain = prompt | model | output_parser

    result = chain.invoke({"query": "Let me know how to cook Bibimbap"})
    print(result)
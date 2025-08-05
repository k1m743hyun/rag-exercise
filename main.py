import os
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import CommaSeparatedListOutputParser

os.environ['GOOGLE_API_KEY'] = ''

if __name__ == '__main__':
    output_parser = CommaSeparatedListOutputParser()
    format_instructions = output_parser.get_format_instructions()
    #print(format_instructions)

    prompt = PromptTemplate(
        template="List five {subject}.\n{format_instructions}",
        input_variables=["subject"],
        partial_variables={"format_instructions": format_instructions},
    )

    model = ChatGoogleGenerativeAI(
        model="gemini-1.5-flash",
        temperature=0,
        max_tokens=200,
    )

    chain = prompt | model | output_parser

    result = chain.invoke({"subject": "popular Korean cusine"})
    print(result)
import os
from langchain_anthropic import ChatAnthropic

os.environ['ANTHROPIC_API_KEY'] = ''

if __name__ == '__main__':
    model = ChatAnthropic(
        model="claude-3-haiku-2024",
        temperature=0,
        max_tokens=200,
    )

    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "LLM은 어떤 원리로 작동하나요? 100자 이내로 설명해주세요."}
    ]

    result = model.invoke(messages)
    print(result)
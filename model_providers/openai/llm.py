from openai import OpenAI
from dotenv import load_dotenv

from ..type import CompletionResponse

## set ENV variables
load_dotenv()
client = OpenAI()

def completion(messages: list[dict[str, str]], tools: dict = None, model="gpt-4o-mini", parallel_tool_calls=True) -> CompletionResponse:
    """因為我覺得要一直用 choices[0] 很煩所以抽象了這一層"""
    create_args = {"model": model, "messages": messages}
    if tools is not None:
        create_args.update({"tools": tools, "parallel_tool_calls": parallel_tool_calls})
    response: ChatCompletion = client.chat.completions.create(**create_args)
    return CompletionResponse(
        response=response,
        message=response.choices[0].message
    )
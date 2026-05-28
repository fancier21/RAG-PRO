import getpass
import os

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

if not os.environ.get("OPENAI_API_KEY"):
    os.environ["OPENAI_API_KEY"] = getpass.getpass("Enter your OpenAI API key: ")


def main():
    llm = ChatOpenAI(model="gpt-5.4-mini")

    first_query = "Hi, I'm Bob."
    messages = [{"role": "user", "content": first_query}]

    response = llm.invoke(messages)
    print(f"Response: {response.text}")


if __name__ == "__main__":
    main()

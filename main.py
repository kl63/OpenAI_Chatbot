import os

import openai
from dotenv import find_dotenv, load_dotenv

# find .env file
dotenv_path = find_dotenv()

# load up the entries as environment variables
load_dotenv(dotenv_path)

# get the OPENAI_API_KEY from environment variable
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# set the api key for openai
openai.api_key = OPENAI_API_KEY

def chat_with_openai(prompt):
    try:
        # Create a chat completion with OpenAI API
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
        )

        # Extract the content of the message from the response
        response_content = response.choices[0].message.content

        # Strip any leading or trailing whitespace from the response content
        response_content_stripped = response_content.strip()

        return response_content_stripped

    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return "Sorry, something went wrong. Please try again."


if __name__ == "__main__":
    while True:
        user_input = input("You: ")

        if user_input.lower() in ["bye", "quit", "exit"]:
            print("CHATBOT: Goodbye!!")
            break

        # Get a response from the OpenAI model
        response = chat_with_openai(user_input)
        print("CHATBOT: ", response)

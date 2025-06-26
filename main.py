import sys
import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
from config import MODEL_NAME
from prompts import SYSTEM_PROMPT


def main():
    load_dotenv()
    
    is_verbose = "--verbose" in sys.argv
    args = [arg for arg in sys.argv[1:] if not arg.startswith("--")]
    if not args:
        print("AI Code Assistant")
        print('\nUsage: python3 main.py "your prompt here" [--verbose]')
        print('Example: python3 main.py "How do I build a calculator app?"')
        sys.exit(1)

    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    user_prompt = " ".join(args)
    
    if is_verbose:
        print(f"User prompt: {user_prompt}")
    
    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]

    generate_content(client, messages, is_verbose)


def generate_content(client, messages, is_verbose):
    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=messages,
        config=types.GenerateContentConfig(system_instruction=SYSTEM_PROMPT)
    )
    if is_verbose:
        prompt_token = response.usage_metadata.prompt_token_count
        response_token = response.usage_metadata.candidates_token_count
        print(f"Prompt tokens: {prompt_token}")
        print(f"Response tokens: {response_token}")
    print("Response:")
    print(response.text)


if __name__ == "__main__":
    main()
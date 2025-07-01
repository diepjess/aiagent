import sys
import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

from config import MODEL_NAME
from config import LOOP_LIMIT
from prompts import SYSTEM_PROMPT
from call_function import available_functions
from call_function import call_function


def main():
    load_dotenv()
    
    is_verbose = "--verbose" in sys.argv
    args = [arg for arg in sys.argv[1:] if not arg.startswith("--")]

    if not args:
        print("AI Code Assistant")
        print('\nUsage: python3 main.py "your prompt here" [--verbose]')
        print('Example: python3 main.py "How do I build a calculator app?"')
        sys.exit(1)
    user_prompt = " ".join(args)

    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)
    
    if is_verbose:
        print(f"User prompt: {user_prompt}")
    
    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]

    generate_content(client, messages, is_verbose)


def generate_content(client, messages, is_verbose):
    for i in range(LOOP_LIMIT):
        response = client.models.generate_content(
            model=MODEL_NAME,
            contents=messages,
            config=types.GenerateContentConfig(
                tools = [available_functions],
                system_instruction=SYSTEM_PROMPT,
            ),
        )
        for candidate in response.candidates:
            message = candidate.content
            messages.append(message)
            print(f"{i + 1}: {message}")
        if not response.function_calls:
            print("Response:")
            print(response.text)
            break
        function_responses = []
        for function_call_part in response.function_calls:
            function_call_result = call_function(function_call_part, verbose=is_verbose)
            try:
                function_call_response = function_call_result.parts[0].function_response.response
            except (AttributeError, IndexError):
                raise Exception("Function call did not return a valid response.")
            messages.append(function_call_result)
            if is_verbose:
                print(f"-> {function_call_response}")
            function_responses.append(function_call_result.parts[0])

    if is_verbose:
        prompt_token = response.usage_metadata.prompt_token_count
        response_token = response.usage_metadata.candidates_token_count
        print(f"Prompt tokens: {prompt_token}")
        print(f"Response tokens: {response_token}")


if __name__ == "__main__":
    main()
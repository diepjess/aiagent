import sys
import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

from config import MODEL_NAME
from config import MAX_ITERS
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
    
    iters = 0
    while True:
        iters += 1
        if iters > MAX_ITERS:
            print(f"Maximum iterations ({MAX_ITERS}) reached.")
            sys.exit(1)
        
        try:
            final_response = generate_content(client, messages, is_verbose)
            if final_response:
                print("Final response")
                print(final_response)
                break
        except Exception as e:
            print(f"Error in generate_content: {e}")


def generate_content(client, messages, is_verbose):
    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=messages,
        config=types.GenerateContentConfig(
            tools = [available_functions],
            system_instruction=SYSTEM_PROMPT,
        ),
    )
    if is_verbose:
        prompt_token = response.usage_metadata.prompt_token_count
        response_token = response.usage_metadata.candidates_token_count
        print(f"Prompt tokens: {prompt_token}")
        print(f"Response tokens: {response_token}")
    function_calls = []
    if response.candidates:
        for candidate in response.candidates:
            function_call_content = candidate.content
            messages.append(function_call_content)
            if function_call_content.parts[0].function_call:
                function_calls.append(function_call_content)
    
    if not function_calls:
        return response.text
    
    function_responses = []
    for function_call_part in function_calls:
        function_call_result = call_function(function_call_part.parts[0].function_call, is_verbose)
        if (
            not function_call_result.parts
            or not function_call_result.parts[0].function_response
        ):
            raise Exception("Error: empty function call result")
        if is_verbose:
            print(f"-> {function_call_result.parts[0].function_response.response}")
        function_responses.append(function_call_result.parts[0])
    
    if not function_responses:
        raise Exception("Error: no function responsed generated, exiting")
    
    messages.append(types.Content(role="tool", parts=function_responses))


if __name__ == "__main__":
    main()
import os
MAX_CHARS = 10000


def get_file_content(working_directory, file_path):
    abs_working_dir = os.path.abspath(working_directory)
    join_path = os.path.join(abs_working_dir, file_path)
    target_file = os.path.abspath(join_path)
    if not target_file.startswith(abs_working_dir):
        return f'Error: Cannot list "{file_path}" as it is outside the permitted working directory'
    if not os.path.isfile(target_file):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    
    try:
        with open(target_file, "r") as f:
            content = f.read(MAX_CHARS + 1)
            if len(content) > MAX_CHARS:
                content = content[:MAX_CHARS]
                was_truncated = True
            else:
                was_truncated = False
    except Exception as e:
        return f"Error: {e}"
    
    message_truncated = f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
    
    return content + (message_truncated if was_truncated else "")
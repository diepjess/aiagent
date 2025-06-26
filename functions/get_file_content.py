import os
from config import MAX_CHARS


def get_file_content(working_directory, file_path):
    abs_working_dir = os.path.abspath(working_directory)
    join_path = os.path.join(abs_working_dir, file_path)
    abs_file_path = os.path.abspath(join_path)
    if not abs_file_path.startswith(abs_working_dir):
        return f'Error: Cannot list "{file_path}" as it is outside the permitted working directory'
    if not os.path.isfile(abs_file_path):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    try:
        with open(abs_file_path, "r") as f:
            content = f.read(MAX_CHARS + 1)
            if len(content) > MAX_CHARS:
                content = content[:MAX_CHARS]
                was_truncated = True
            else:
                was_truncated = False
        message_truncated = f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
        return content + (message_truncated if was_truncated else "")
    except Exception as e:
        return f"Error: {e}"
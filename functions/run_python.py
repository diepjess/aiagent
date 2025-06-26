import os
import subprocess
from google.genai import types


def run_python_file(working_directory, file_path, args=None):
    abs_working_dir = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))
    if not abs_file_path.startswith(abs_working_dir):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    if not os.path.exists(abs_file_path):
        return f'Error: File "{file_path}" not found.'
    if not file_path.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file.'
    try:
        commands = ["python3", abs_file_path]
        if args:
            commands.extend(args)
        result = subprocess.run(
            commands,
            cwd=abs_working_dir,
            capture_output=True,
            timeout=30,
            text=True,
        )
        result_stdout = result.stdout.decode("utf-8")
        result_stderr = result.stderr.decode("utf-8")
        result_code = result.returncode
        if not result_stdout and not result_stderr:
            return f"No output produced."
        output = "\n".join([f"STDOUT:\n{result_stdout}", f"STDERR:\n{result_stderr}"])
        return output + (f"\nProcess exited with code {result_code}" if result_code != 0 else "")
    except Exception as e:
        return f"Error: executing Python file: {e}"


schema_run_python_file = types.FunctionDeclaration(
        name="run_python_file",
        description="Executes Python files, constrained to the working directory.",
        parameters=types.Schema(
            type=types.Type.OBJECT,
            properties={
                "run": types.Schema(
                    type=types.Type.STRING,
                    description="Executes python files with optional arguments, relative to the working directory.",
                ),
            },
        ),
    )
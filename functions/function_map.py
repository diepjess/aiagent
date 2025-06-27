from functions.get_file_content import get_file_content
from functions.get_files_info import get_files_info
from functions.run_python import run_python_file
from functions.write_file import write_file


function_map = {
    "get_file_content": get_file_content,
    "get_file_info": get_files_info,
    "run_python_file": run_python_file,
    "write_file": write_file,
}
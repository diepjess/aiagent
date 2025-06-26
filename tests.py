from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.write_file import write_file
from functions.run_python import run_python_file

    
def test_get_files_info():
    result = get_files_info("calculator", ".")
    print("Result for calculator directory:")
    print(result)
    print()

    result = get_files_info("calculator", "pkg")
    print("Result for 'pkg' directory:")
    print(result)
    print()

    result = get_files_info("calculator", "/bin")
    print("Result for '/bin' directory:")
    print(result)
    print()

    result = get_files_info("calculator", "../")
    print("Result for '../' directory:")
    print(result)
    print()
    
    result = get_files_info("calculator", "main.py")
    print("Result for 'main.py' directory:")
    print(result)
    print()
    
    result = get_files_info("main.py")
    print("Result for main.py direcotyr")
    print(result)
    print()


def test_get_file_content():
    result = get_file_content("calculator", "lorem.txt")
    print('Result from "lorem.txt"')
    print(result)

    result = get_file_content("calculator", "main.py")
    print('Result from "main.py"')
    print(result)
    
    result = get_file_content("calculator", "pkg/calculator.py")
    print('Result from "pkg/calculator.py"')
    print(result)
    
    result = get_file_content("calculator", "/bin/cat")
    print('Result from "/bin/cat"')
    print(result)


def test_write_file():
    result = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
    print('Result from "lorem.txt')
    print(result)
    
    result = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
    print('Result from "pkg/morelorem.txt')
    print(result)
    
    result = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
    print('Result from "/tmp/temp.txt"')
    print(result)


def test_run_python():
    result = run_python_file("calculator", "main.py")
    print('Result from "main.py"')
    print(result)
    
    result = run_python_file("calculator", "tests.py")
    print('Result from "tests.py"')
    print(result)
    
    result = run_python_file("calculator", "../main.py")
    print('Result from "../main.py"')
    print(result)
    
    result = run_python_file("calculator", "nonexistent.py")
    print('Result from "nonexistent.py"')
    print(result)

if __name__ == "__main__":
    test_run_python()
from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content

    
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


if __name__ == "__main__":
    test_get_file_content()
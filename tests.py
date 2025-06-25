from functions.get_files_info import get_files_info

    
def test():
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


if __name__ == "__main__":
    test()
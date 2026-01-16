FILE_NAME = "example.txt"


def read_file():
    with open(FILE_NAME, "r", encoding="utf-8") as file:
        print("--- Reading file ---")
        print(file.read())


def overwrite_file():
    with open(FILE_NAME, "w", encoding="utf-8") as file:
        file.write("This content overwrote the previous file.\n")
    print("--- File overwritten ---")


def append_file():
    text = input("Write text to append: ")
    with open(FILE_NAME, "a", encoding="utf-8") as file:
        file.write(text + "\n")
    print("--- Text appended ---")


read_file()
overwrite_file()
read_file()
append_file()
read_file()

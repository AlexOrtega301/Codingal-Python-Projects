def read_full_file():
    with open("example.txt", "r", encoding="utf-8") as file:
        print("--- read() ---")
        print(file.read())


def read_line_by_line():
    with open("example.txt", "r", encoding="utf-8") as file:
        print("\n--- for line in file ---")
        for line in file:
            print(line.strip())


def read_lines_list():
    with open("example.txt", "r", encoding="utf-8") as file:
        print("\n--- readlines() ---")
        lines = file.readlines()
        for line in lines:
            print(line.strip())


read_full_file()
read_line_by_line()
read_lines_list()

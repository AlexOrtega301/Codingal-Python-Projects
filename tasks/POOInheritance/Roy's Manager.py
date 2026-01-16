class FileHandler:
    def __init__(self, filename):
        self.filename = filename

    def read_file(self):
        try:
            with open(self.filename, "r") as file:
                content = file.read()
            print("\n📄 Current content of the file:")
            print(content)
        except FileNotFoundError:
            print("⚠️ File not found. A new one will be created.")

    def write_file(self, text):
        with open(self.filename, "w") as file:
            file.write(text)
        print("\n✅ File overwritten successfully.")

    def append_file(self, text):
        with open(self.filename, "a") as file:
            file.write(text)
        print("\n✅ Text appended successfully.")

class Roy(FileHandler):
    def __init__(self, filename):
        super().__init__(filename)

    def overwrite_students(self):
        print("\n📝 Enter new list of students.")
        print("Type 'done' when finished.")
        new_content = ""
        while True:
            line = input("Enter student and favorite subject (ex: Alex, Favorite Subject: Math): ")
            if line.lower() == "done":
                break
            new_content += line + "\n"
        self.write_file(new_content)

    def add_student(self):
        print("\n➕ Add a single student description.")
        extra = input("Enter student and favorite subject: ")
        self.append_file(extra + "\n")

filename = "MyFile.txt"
roy = Roy(filename)
#This is what will be displayed.
print("=== Student File Manager for Roy ===")
roy.read_file()

while True:
    print("\nChoose an option:")
    print("1 - Overwrite entire file")
    print("2 - Add a new student")
    print("3 - Show file content")
    print("4 - Quit")

    choice = input("Option: ")

    if choice == "1":
        roy.overwrite_students()

    elif choice == "2":
        roy.add_student()

    elif choice == "3":
        roy.read_file()

    elif choice == "4":
        print("✨ Finished. Have a great day!")
        break

    else:
        print("⚠️ Invalid choice, try again!")

import keyword

# Check if a word is a Python keyword
word = input("Enter a word: ")

print("\nChecking keyword status...\n")
print(keyword.iskeyword(word))
#check to see if the user wants to see the list of all Python keywords
check = input("\nDo you want to see the list of all Python keywords? (yes/no): ")
if check.lower() == 'yes':
    print("\nList of Python keywords:\n")
    print(keyword.kwlist)
else:
    print("\nOkay, have a great day!")
#end of program1.0

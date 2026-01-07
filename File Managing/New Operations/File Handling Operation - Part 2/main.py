  #create a new file
import os
if os.path.exists("Cool_file.txt"):
  os.remove("Cool_file.txt")
new_file = open('Cool_File.txt', 'x')
new_file.close()

#check if a file exists 

print("Checking if my_file exists or not....")
if os.path.exists("old.txt"):
  os.remove("old.txt")
else:
  print("The file does not exist")

#create a new if it doesn't
my_file = open("old.txt", "w")
my_file.write("Placeholder.")
my_file.close()

#delete file named TMAFE.txt
os.remove('TMAFE.txt')

#delete the folder
os.rmdir('Folder')


# write in file using with()function
with open('Windows.txt', 'w') as file:
  file.write("\n Hi! I am Alex and I am 13 yr old.")
file.close()

# split file into words
with open('Windows.txt', 'r') as file:
  data = file.readlines()
  print("Words in this file are....")
  for line in data:
    word = line.split()
    print (word)
file.close()


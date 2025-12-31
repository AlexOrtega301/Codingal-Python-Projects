# open the file in read mode
file_read = open('Codingal.txt','r')
print("File in Read Mode -")
print(file_read.read())
file_read.close()

# open the file in write mode
file_write = open('Codingal.txt', 'w')
# write in the file 
file_write.write("\n File in write mode ....")
file_write.write("\n Hi! I am Alex. I am 14 yr. old ")
file_write.close()

# open the file in append mode
file_append = open('Codingal.txt', 'a')
# append in the file 
file_append.write("\n File in append mode ....")
file_append.write("\n I love coding and problem solving.")
file_append.close()


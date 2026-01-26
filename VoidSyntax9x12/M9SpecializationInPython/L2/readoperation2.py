file_read = open("VoidSyntax9x12/M9SpecializationInPython/L2/Codingal2.txt", "r")
print("File in read mode - ")
print(file_read.read())
file_read.close()

file_write = open("VoidSyntax9x12/M9SpecializationInPython/L2/Codingal2.txt", "w")
print("File in write mode - ")
file_write.write("Hi! I am Penguine. I am 1 year old.")
file_write.close()

file_append = open("VoidSyntax9x12/M9SpecializationInPython/L2/Codingal2.txt", "a")
print("File in append mode - ")
file_append.write("\nHi! I am Koala. I am 2 year old.")
file_append.close()
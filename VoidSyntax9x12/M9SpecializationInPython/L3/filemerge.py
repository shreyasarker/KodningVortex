

with open("VoidSyntax9x12/M9SpecializationInPython/L3/file1.txt", "r") as file1:
    data1 = file1.read()

with open("VoidSyntax9x12/M9SpecializationInPython/L3/file2.txt", "r") as file2:
    data2 = file2.read()

data = data1 + "\n" + data2
print("Merging the contents of two files into a new file: ")
with open("VoidSyntax9x12/M9SpecializationInPython/L3/file3.txt", "w") as file3:
    file3.write(data)

file1.close()
file2.close()   
file3.close()
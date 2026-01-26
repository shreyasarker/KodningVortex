file1 = open("VoidSyntax9x12/M9SpecializationInPython/L2/Codingal1.txt", "r")
file2 = open("VoidSyntax9x12/M9SpecializationInPython/L2/Codingal_Updated2.txt", "w")

content = file1.readlines()
for i in range(1, len(content)+1):
    if i % 2 != 0:
        file2.write(content[i-1])
    else:
        pass    

file1.close()
file2.close() 

file2 = open("VoidSyntax9x12/M9SpecializationInPython/L2/Codingal_Updated2.txt", "r")  
print("The odd lines from the file are: ")
print(file2.read())
file2.close()
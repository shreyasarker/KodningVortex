file1 = open("VoidSyntax9x12/M9SpecializationInPython/L2/Codingal1.txt", "r")
file2 = open("VoidSyntax9x12/M9SpecializationInPython/L2/Codingal_Updated.txt", "w")

for line in file1.readlines():
    if not (line.startswith("Coding")):
        print(line)
        file2.write(line)

file1.close()
file2.close()   
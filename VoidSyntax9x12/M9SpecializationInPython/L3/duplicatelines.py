file1 = open("VoidSyntax9x12/M9SpecializationInPython/L3/Codingal_Repeated.txt", "r")
file2 = open("VoidSyntax9x12/M9SpecializationInPython/L3/Codingal_Updated.txt", "w")

lines_seen = set()
print("Eliminating duplicate lines from the file: ")
for line in file1:
    if line not in lines_seen:
        file2.write(line)
        lines_seen.add(line)   

file1.close()
file2.close() 
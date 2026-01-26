file = open("VoidSyntax9x12/M9SpecializationInPython/L1/Codingal1.txt")
counter = 0

content = file.read()
content_list = content.split("\n")

for i in content_list:
    if i:
        counter += 1
print("Number of lines in the file:", counter)
file.close()
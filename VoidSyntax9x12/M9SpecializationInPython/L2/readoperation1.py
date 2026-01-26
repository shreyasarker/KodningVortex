file = open("VoidSyntax9x12/M9SpecializationInPython/L2/Codingal1.txt", "r")
print(file.read())
file.close()

file = open("VoidSyntax9x12/M9SpecializationInPython/L2/Codingal1.txt", "r")
print("Read in parts - ")
print(file.read(8))
file.close()

file = open("VoidSyntax9x12/M9SpecializationInPython/L2/Codingal1.txt", "a")
file.write("Hi! I am Penguine. I am 1 year old.")
file.close()
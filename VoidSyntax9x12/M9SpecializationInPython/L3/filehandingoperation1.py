with open("VoidSyntax9x12/M9SpecializationInPython/L3/Codingal1.txt", "w") as file:
    file.write("Hi! I am Penguine. I am 1 year old.")
file.close()    

with open("VoidSyntax9x12/M9SpecializationInPython/L3/Codingal1.txt", "r") as file:
    data = file.readlines()
    print("Words in tis file are:")
    for line in data:
        word = line.split()
        print(word)
file.close() 
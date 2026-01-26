new_file = open("VoidSyntax9x12/M9SpecializationInPython/L3/New_File.txt", "x")
new_file.close()

import os
print("Checking if the file exists or not: ")
if os.path.exists("VoidSyntax9x12/M9SpecializationInPython/L3/My_File.txt"):
    print("File exists.")
    os.remove("VoidSyntax9x12/M9SpecializationInPython/L3/My_File.txt")
else:
    print("File does not exist.")

my_file = open("VoidSyntax9x12/M9SpecializationInPython/L3/My_File.txt", "w")
my_file.write("This is my new file.")
my_file.close()   

os.remove("VoidSyntax9x12/M9SpecializationInPython/L3/Codingal2.txt")
os.rmdir("VoidSyntax9x12/M9SpecializationInPython/L3/Folder")
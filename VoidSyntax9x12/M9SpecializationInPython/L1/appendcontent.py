f1 = open("VoidSyntax9x12/M9SpecializationInPython/L1/file1.txt", "r")
f2 = open("VoidSyntax9x12/M9SpecializationInPython/L1/file2.txt", "r")

print("Contents of file1 before appending:\n", f1.read())
print("Contents of file2 before appending:\n", f2.read())

f1.close()
f2.close()

f1 = open("VoidSyntax9x12/M9SpecializationInPython/L1/file1.txt", "a+")
f2 = open("VoidSyntax9x12/M9SpecializationInPython/L1/file2.txt", "r")

f1.write(f2.read())

f1.seek(0)
f2.seek(0)

print("Contents of file1 after appending:\n", f1.read())
print("Contents of file2 remains unchanged:\n", f2.read())

f1.close()
f2.close()
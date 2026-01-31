def areEqual(a, b):
    # XOR gives 0 only when both numbers are equal
    if (a ^ b) == 0:
        print("Both numbers are equal")
    else:
        print("Numbers are not equal")


num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

areEqual(num1, num2)

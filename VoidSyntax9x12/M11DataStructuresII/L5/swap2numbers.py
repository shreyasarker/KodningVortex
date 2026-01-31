def swap_xor(a, b):
    print("Before swap:")
    print("a =", a, "b =", b)

    a = a ^ b
    b = a ^ b
    a = a ^ b

    print("After swap:")
    print("a =", a, "b =", b)


x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

swap_xor(x, y)

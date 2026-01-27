def find_gcd(a, b):
    while b != 0:
        temp = b              # store value of b
        remainder = a % b     # find remainder
        a = temp              # update a
        b = remainder         # update b
    return a

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

print("HCF or GCD is:", find_gcd(x, y))

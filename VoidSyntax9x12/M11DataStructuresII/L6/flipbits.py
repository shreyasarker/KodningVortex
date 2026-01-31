def totalFlips(number1, number2):
    xor = number1 ^ number2
    flips = 0

    while xor > 0:
        flips += xor & 1
        xor >>= 1

    return flips


number1 = int(input("Enter First number: "))
number2 = int(input("Enter Second number: "))

print("Number of flips needed:", totalFlips(number1, number2))

def isNthBitSet(number, n):
    if number & (1 << n):
        print(f"The {n}th bit is SET (1)")
    else:
        print(f"The {n}th bit is NOT SET (0)")


num = int(input("Enter the number: "))
n = int(input("Enter the bit position (starting from 0): "))

isNthBitSet(num, n)

def isPowerOfTwo(n):
    # n must be positive and only one bit should be set
    if n > 0 and (n & (n - 1)) == 0:
        print(n, "is a power of 2")
    else:
        print(n, "is NOT a power of 2")


num = int(input("Enter a number: "))
isPowerOfTwo(num)

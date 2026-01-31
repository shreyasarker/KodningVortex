def isPowerOfFour(n):
    if n <= 0:
        return False

    # must be power of 2
    if (n & (n - 1)) != 0:
        return False

    count = 0
    while n > 1:
        n >>= 1
        count += 1

    # power of 4 → even number of shifts
    return count % 2 == 0


num = int(input("Enter a number: "))

if isPowerOfFour(num):
    print(num, "is a power of 4")
else:
    print(num, "is NOT a power of 4")

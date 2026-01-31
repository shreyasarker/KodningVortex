def twoOddOccurring(arr):
    xor_all = 0

    # Step 1: XOR all elements → result = a ^ b
    for num in arr:
        xor_all ^= num

    # Step 2: Get rightmost set bit
    rightmost_set_bit = xor_all & -xor_all

    x = 0
    y = 0

    # Step 3: Divide elements into two groups
    for num in arr:
        if num & rightmost_set_bit:
            x ^= num
        else:
            y ^= num

    return x, y


arr = []
n = int(input("Enter array size: "))

while n > 0:
    arr.append(int(input("Enter number: ")))
    n -= 1

a, b = twoOddOccurring(arr)
print("Two odd occurring numbers are:", a, "and", b)

def power_bitwise(x, y):
    # This version assumes y >= 0 (non-negative exponent)
    result = 1

    while y > 0:
        # If y is odd, multiply result by current x
        if (y & 1) == 1:
            result *= x

        # Square x and halve y
        x *= x
        y >>= 1

    return result


x = int(input("Enter x: "))
y = int(input("Enter y (non-negative): "))

print("x ^ y =", power_bitwise(x, y))

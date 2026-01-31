def divide_bitwise(dividend, divisor):
    if divisor == 0:
        print("Division by zero is not allowed")
        return

    # Handle negative result
    negative = (dividend < 0) ^ (divisor < 0)

    dividend = abs(dividend)
    divisor = abs(divisor)

    quotient = 0

    # Try every bit position from high to low
    for i in range(31, -1, -1):
        if (divisor << i) <= dividend:
            dividend -= (divisor << i)
            quotient |= (1 << i)

    if negative:
        quotient = -quotient

    print("Quotient:", quotient)

a = int(input("Enter dividend: "))
b = int(input("Enter divisor: "))
divide_bitwise(a, b)

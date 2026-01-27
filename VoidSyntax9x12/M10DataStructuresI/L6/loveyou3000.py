a = 3000

for num in range(2, a + 1):
    # PRIME CHECK
    is_prime = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        # PALINDROME CHECK
        temp = num
        rev = 0
        while temp > 0:
            rev = rev * 10 + (temp % 10)
            temp //= 10

        if rev == num:
            print(num)

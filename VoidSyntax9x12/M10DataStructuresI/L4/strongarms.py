num = int(input("Enter a number: "))

# Store the original number
original = num

# Find number of digits
digits = len(str(num))

sum = 0

while num > 0:
    digit = num % 10
    sum += digit ** digits
    num //= 10

if sum == original:
    print(original, "is an Armstrong number")
else:
    print(original, "is not an Armstrong number")

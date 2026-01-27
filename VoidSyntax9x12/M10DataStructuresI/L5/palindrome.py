def is_palindrome(num):
    original = num
    reverse = 0

    while num > 0:
        digit = num % 10
        reverse = reverse * 10 + digit
        num //= 10

    if original == reverse:
        return True
    else:
        return False


number = int(input("Enter a number: "))

if is_palindrome(number):
    print(number, "is a palindrome number")
else:
    print(number, "is not a palindrome number")

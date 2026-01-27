def find_factors(num):
    print("Factors of", num, "are:")
    for i in range(1, num + 1):
        if num % i == 0:
            print(i)

# Taking input
number = int(input("Enter a number: "))
find_factors(number)

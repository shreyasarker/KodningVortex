num_str = input("Enter a number to check: ")
num_length = len(num_str)
number = int(num_str)

# Initialize sum
sum_of_powers = 0

# Temporary variable to store the original number
temp = number

while temp > 0:
    # Get the last digit
    digit = temp % 10
    
    # Add the digit raised to the power of num_length to the sum
    sum_of_powers += digit ** num_length
    
    # Remove the last digit from temp
    temp //= 10

# Check and display the result
if number == sum_of_powers:
    print(f"Yes! {number} is an Armstrong number.")
else:
    print(f"No, {number} is not an Armstrong number.")
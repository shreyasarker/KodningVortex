x = int(input("Enter 1st number: "))
y = int(input("Enter 2nd number: "))
z = int(input("Enter 3rd number: "))

print(f"Original values: x={x}, y={y}, z={z}")

# Step 1: Compare x and y
if x > y:
    x, y = y, x

# Step 2: Compare x and z (to ensure the smallest is in x)
if x > z:
    x, z = z, x

# Step 3: Compare y and z (to ensure y is less than z)
if y > z:
    y, z = z, y

# Printing the updated values
print(f"Updated values: x={x}, y={y}, z={z}")
def func1(n):
    iterations = 0
    result = n * (n + 1) // 2
    iterations += 1
    print("Iterations in func1:", iterations)
    return result

print(func1(5))
# No loop, Executes only once, Iterations = 1
# Time Complexity: O(1) (constant time)

def func2(n):
    iterations = 0
    sum = 0
    for i in range(1, n + 1):
        iterations += 1
        sum += i
    print("Iterations in func2:", iterations)
    return sum    

print(func2(5))
# Loop runs n times, Iterations = n
# For n = 5 → iterations = 5
# Time Complexity: O(n) (linear time)


def func3(n):
    iterations = 0
    sum = 0
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            iterations += 1
            sum += 1
    print("Iterations in func3:", iterations)        
    return sum

print(func3(5))
# Nested loops, Total iterations: 15
# For n = 5 → iterations = 15
# Time Complexity: O(n²) (quadratic time)

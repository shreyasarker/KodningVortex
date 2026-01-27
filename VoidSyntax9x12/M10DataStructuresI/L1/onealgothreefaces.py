def func1(n):
    return n * (n + 1) // 2

print(func1(5))
# 5 * (5 + 1) // 2 = 15

def func2(n):
    sum = 0
    for i in range(1, n + 1):
        sum += i
    return sum    

print(func2(5))
# 1 + 2 + 3 + 4 + 5 = 15

def func3(n):
    sum = 0
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            sum += 1
    return sum

print(func3(5))
# 1 + (1 + 2) + (1 + 2 + 3) + (1 + 2 + 3 + 4) + (1 + 2 + 3 + 4 + 5) = 15
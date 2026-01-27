def sum(n):
    return n * (n + 1) // 2

sum(5)
# Space Complexity: O(1), Time Complexity: O(1)

def arraysum(a):
    sum = 0
    for i in a:
        sum += i
    return sum

a = [12, 3, 4, 15]
arraysum(a)
# Space Complexity: O(1), Time Complexity: O(n)

def recursivesum(n):
    if n <= 0:
        return 0
    else:
        return n + recursivesum(n - 1)
    
recursivesum(5)
# Space Complexity: O(n), Time Complexity: O(n)    
def OddOccurring(arr):
    res = 0

    for element in arr:
        # XOR with the result
        res = res ^ element
 
    return res
 
arr = []
 
# Take array size as input
n = int(input("Enter array size : "))
 
# Take array element input 
while(n):
    num = int(input("Enter number : "))
    arr.append(num)
    n-=1
 
print("Odd occurring number is : ",OddOccurring(arr))
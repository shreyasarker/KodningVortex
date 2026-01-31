def printPowerSet(arr, n):
    powerSetSize = 1 << n   # 2^n

    for mask in range(powerSetSize):
        for i in range(n):
            if (mask & (1 << i)) > 0:
                print(arr[i], end=" ")
        print() 


size = int(input("Enter array size: "))

arr = []
for i in range(size):
    num = int(input("Enter element: "))
    arr.append(num)

printPowerSet(arr, len(arr))

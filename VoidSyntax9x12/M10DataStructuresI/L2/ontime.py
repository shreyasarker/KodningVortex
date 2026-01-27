def ontime(n):
    iterations = 0
    for i in range(1, n + 1):
        iterations += 1
    print("When n is", n, " Iterations is", iterations)

ontime(10)
ontime(20)
ontime(40)

print("\n As 'n' increases, the iterations also increase linearly.")
    
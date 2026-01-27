def onsquare(n):
    iterations = 0
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            print("*", end=" ")
            iterations += 1
        print()
    print("When n is", n, "Iterations is", iterations)   

onsquare(5)         
onsquare(10)         
onsquare(5)         

print("\n As 'n' increases, the iterations increase quadratically. With every 'n', the time taken equals n ^ 2.")
print("O(n^2)")
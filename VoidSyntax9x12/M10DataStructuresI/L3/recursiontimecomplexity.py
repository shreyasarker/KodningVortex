def printnumber(n):
    if n <= 0:
        return
    else:
        print("The value of 'n' is", n)
        printnumber(n // 2)
        printnumber(n // 2)

printnumber(8)        

# Level 0:        8        → 1 call
# Level 1:     4     4     → 2 calls
# Level 2:   2  2  2  2    → 4 calls
# Level 3: 1 1 1 1 1 1 1 1 → 8 calls
# Total calls: 1 + 2 + 4 + 8 = 15 ≈ 2n − 1
# Time Complexity: O(n)
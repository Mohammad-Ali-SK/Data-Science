

def sumN(n):
    if n == 1:
        return 1
    return 2*n + sumN(n-1)

print(sumN(10))
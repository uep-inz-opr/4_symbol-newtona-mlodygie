import math

n, k = [int(n) for n in input().split()]

def newton(n,k):
    return math.factorial(n)/(math.factorial(k)*math.factorial(n-k))

print(newton(n, k))
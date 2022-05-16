import math

n, k = [int(n) for n in input().split()]
    
print(math.factorial(n)/(math.factorial(k)*math.factorial(n-k)))
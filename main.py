import math

zmienne = map(int, input().split())
x = list(zmienne)

n = x[0]
k = x[1]
nk = n-k

wynik_n = []
wynik_k = []
wynik_nk = []

while n >= 1:
    wynik_n.append(n)
    n = n-1

while k >= 1:
    wynik_k.append(k)
    k = k-1

while nk >= 1:
    wynik_nk.append(nk)
    nk = nk-1

silnia_n = math.prod(wynik_n)
silnia_k = math.prod(wynik_k)
silnia_nk = math.prod(wynik_nk)

newton = (silnia_n/(silnia_k*silnia_nk))

print(int(newton))
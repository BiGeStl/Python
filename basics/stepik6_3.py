import math

a = float(input())
b = float(input())

Sra = (a + b) / 2
Srg = math.sqrt(a * b)
Srgar = (2 * a * b) / (a + b)
Srq = math.sqrt(((a**2) + (b**2)) / 2)

print(Sra)
print(Srg)
print(Srgar)
print(Srq)
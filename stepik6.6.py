import math #Можно было не писать наверное это, потому что я не использовал sqrt, но тема так называется. Вместо sqrt, взял D ** 0.5

a = float(input())
b = float(input())
c = float(input())

D = ((b**2) - 4 * a * c)

if D < 0: 
    print("Нет корней")
elif D == 0:
    x = -b / (2*a)
    print(x)
else:
    x1 = (((-b + (D ** 0.5)))/(2*a))
    x2 = (((-b - (D ** 0.5)))/(2*a))
    print(min(x1,x2))
    print(max(x1,x2))
    
    



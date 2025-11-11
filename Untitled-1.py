a = input()
b = input()

if a == b:
    print("Пароль принят")
else:
    print("Пароль не принят")




i = int(input())

if i % 2 == 0:
    print('Четное')
else:
    print('Нечетное')




num = int(input())

a = num % 10
b = (num // 10) % 10 
c = (num // 100) % 10
d = num // 1000

q = a + d
w = b + c

if(w > q):
    print('ДА')
else: 
    print('НЕТ')

age = int(input())

if (age >= 18):
    print("Доступ разрешен")
else:
    print("Доступ запрещен")



a = int(input())
b = int(input())
c = int(input())

if b - a == c - b:
    print("YES")
else:
    print("NO")




a = int(input())
b = int(input())

if (a > b):
    print(b)
else: 
    print(a)





a = int(input())
b = int(input())
c = int(input())
d = int(input())


if a < b:
    min_ab = a
else:
    min_ab = b
    
if c < d:
    min_cd = c
else:
    min_cd = d
    
if min_ab < min_cd:
    min_abcd = min_ab
else: 
    min_abcd = min_cd
print(min_abcd)






a = int(input())
b = int(input())
c = int(input())
d = int(input())


if a < b:
    min_ab = a
else:
    min_ab = b
    
if c < d:
    min_cd = c
else:
    min_cd = d
    
if min_ab < min_cd:
    min_abcd = min_ab
else: 
    min_abcd = min_cd
print(min_abcd)





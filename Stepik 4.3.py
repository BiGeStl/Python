"6 Задание"

a = int(input())
b = int(input())
c = input()

if c != "*" and c != "-" and c != "+" and c != "/":
    print("Неверная операция")

if c == "*" :
    print(a * b)
elif c == "-":
    print(a - b)
elif c == "+":
    print(a + b)
elif c == "/" :
    if b != 0:
        print(a / b)
    else:
        print("На ноль делить нельзя!")
    

        
    


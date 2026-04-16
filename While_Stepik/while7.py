# Обратный порядок 2


num = int(input())

product = 1
while num != 0:
    last_digit = num % 10
    num = num // 10
    print(last_digit, end = "")
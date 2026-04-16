# Дано натуральное число. Напишите программу, которая вычисляет:

# сумму его цифр;
# количество цифр в нем;
# произведение его цифр;
# среднее арифметическое его цифр;
# его первую цифру;
# сумму его первой и последней цифры.
# Формат входных данных
# На вход программе подаётся натуральное число.

# Формат выходных данных
# Программа должна вывести значения указанных величин в указанном порядке, каждое на отдельной строке.

num = int(input("Введите натуральное число: "))

original = num

sum_digits = 0       # сумма цифр
count_digits = 0     # количество цифр
product_digits = 1   # произведение цифр

last_digit = num % 10  # последняя цифра

while num > 0:
    digit = num % 10       # последняя цифра
    sum_digits += digit
    product_digits *= digit
    count_digits += 1
    num //= 10             # убираем последнюю цифру

# Найдём первую цифру
first_digit = original
while first_digit >= 10:
    first_digit //= 10

# Сумма первой и последней цифры
sum_first_last = first_digit + last_digit

# Среднее арифметическое
average_digits = sum_digits / count_digits

# Вывод результатов
print(sum_digits)
print(count_digits)
print(product_digits)
print(average_digits)
print(first_digit)
print(sum_first_last)

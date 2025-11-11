# Количество пятёрок 5️⃣

total = 0

n = int(input())
while n > 0 and n <= 5:   
    if n == 5:
        total += 1
    n = int(input())    

print(total)

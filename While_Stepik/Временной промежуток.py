h1 = int(input())
m1 = int(input())
h2 = int(input())
m2 = int(input())

start = h1 * 60 + m1
end = h2 * 60 + m2

while start <= end:
    h = start // 60
    m = start % 60

    # тут вывод
    print(f"{h:02}:{m:02}")

    start += 1

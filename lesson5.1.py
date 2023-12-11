x = int(input('Введить число: '))

count = 0
y = 1
while y <= x:
    if y % 3 != 0:
        count += y ** 3
    y += 1
print('Результат: ', count)

c = 0
for i in range(1, x+1):
    if i % 3 != 0:
        c += i ** 3
print('Результат: ', c)


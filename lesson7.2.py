x = int(input('Введить число: '))

a = lambda x: 'парне' if x % 2 == 0 else 'непарне'


print(f'Ви ввели {a(x)} число.')



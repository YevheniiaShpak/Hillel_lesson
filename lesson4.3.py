x = input('Введить число: ')

if x.isdigit():
    number = int(x)
    parity = 'парне' if number % 2 == 0 else 'непарне'
    print(f'Ви ввели {parity} число.')

else:
    print("Не вірне введення.")


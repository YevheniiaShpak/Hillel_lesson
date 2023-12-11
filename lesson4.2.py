name = input('Вітаю! Як Ваше ім"я? ')

while True:
    age = input('Скільки Вам років? ')
    if not age.isdigit() or int(age) == 0:
        print('Помилка, повторіть введення: ')
        continue
    elif int(age) < 10:
        print(f'Привіт, шкет {name}')
        continue
    elif 10 <= int(age) <= 18:
        print(f'Як справи, {name} ?')
        continue
    elif 18 < int(age) < 100:
        print(f'Що бажаєте {name}?')
        continue
    else:
        print(f'{name}, ви брешете - у наш час стільки не живуть...')
        a = input ('Бажаєте вийти? Д/Y ').upper()
        if a == 'Д' or a == 'Y':
            break


def new_input(x1):
    if x1.isdigit():
        number = int(x1)
        return f"Ви ввели ціле число: {number}"
    elif x1.replace('.', '', 1).isdigit() or x1.replace(',', '', 1).isdigit():
        number1 = float(x.replace(',', '.'))
        if number1 == 0:
            return "Ви ввели нуль"
        elif number1 < 0:
            return f"Ви ввели від'ємне {'дробове' if '.' in x1 else 'ціле'} число: {number1}"
        else:
            return f"Ви ввели {'дробове' if '.' in x1 else 'ціле'} число: {number1}"
    else:
        return f"Ви ввели не коректне число: {x1}"


while True:
    x = input("Введіть число або 'вихід', 'exit', 'quit', 'e', або 'q': ").lower()
    if x in ['вихід', 'exit', 'quit', 'e', 'q']:
        print("Вихід з програми.")
        break
    result = new_input(x)
    print(result)



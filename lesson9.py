def new_input(x1):
    if x1.replace('.', '', 1).replace(',', '', 1).lstrip('-').isdigit():
        number = float(x1.replace(',', '.'))
        if '.' in x1 or ',' in x1:
            return f"Ви ввели {'від\'ємне ' if number < 0 else 'позитивне'} дробове число: {number}"
        elif number == 0:
            return "Ви ввели нуль"
        else:
            return f"Ви ввели {'від\'ємне ' if number < 0 else 'позитивне'} ціле число: {int(number)}"
    else:
        return f"Ви ввели неправильне число: {x1}"


while True:
    x = input("Введіть число або 'вихід', 'exit', 'quit', 'e', або 'q': ").lower()
    if x in ['вихід', 'exit', 'quit', 'e', 'q']:
        print("Вихід з програми.")
        break
    result = new_input(x)
    print(result)



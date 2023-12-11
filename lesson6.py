from random import randint
def guess():
    x = randint(0, 9)
    print(x)      #щоб побачити загадане число рандому
    return x
y = guess()
while True:
    i = int(input('Привіт!Я загадав цифру, вгадай її: '))
    if i == y:
        print('Ура вгадав!')
        break
    elif i > y:
        print('Моє число меньше:)')
    elif i < y:
        print('Моє число більше:)')



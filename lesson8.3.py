import time, math


def decor (func):
    def wrapper():
        start = time.time()
        result = func()
        end = time.time()
        total = end - start
        print(f"Час виконання {func.__name__}: {total} секунд")
        return result
    return wrapper

PI = math.pi
D = float(input("Диаметр циліндра,см: "))
H = float(input("Висота циліндра,см: "))


@decor
def radius():
    r = D/2
    time.sleep(1)
    return r


@decor
def volume():
    r = radius()
    s = PI*r**2
    V = round(s*H, 2)
    time.sleep(1)
    return V


print("Об'єм циліндра дорівнює", volume(), "см3")


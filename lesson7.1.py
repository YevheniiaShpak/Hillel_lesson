from random import randint

m = [randint(1, 10) for i in range(200)]
def count():
    a = {}
    for elem in m:
        a[elem] = a.get(elem, 0) + 1
    return a
co = count()
print(co)

form = lambda count: "раз" if count == 1 else "разів" if 1 < count < 5 else "раза"
for number in sorted(co):
    val = co[number]
    print(f"Число {number} зустрічається у початковому списку {val} {form(val)}")


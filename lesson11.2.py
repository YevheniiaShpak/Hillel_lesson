import csv, json, random

with open("dz18.json", "r") as f:
    a = json.load(f)

with open('dz19.csv', 'w', newline='') as csv_f:
    names = ['ID', 'Ім\'я', 'Вік', 'Телефон']
    writer = csv.DictWriter(csv_f, fieldnames=names, delimiter=',')
    writer.writeheader()

    for ID, (name, age) in a.items():
        has_phone = random.choice([True, False])
        phone = random.choice(['095', '066', '098', '096', '050', '097']) + ''.join(
            random.choices('0123456789', k=7)) if has_phone else ''
        writer.writerow({'ID': ID, 'Ім\'я': name, 'Вік': age, 'Телефон': phone})

print('Дані були успішно записані у CSV-файл.')

from datetime import datetime


class Person:

    def __init__(self, name, second_name=None, surname=None, birth_date=None, death_date=None, gender=None):
        self.name = name
        self.second_name = second_name
        self.surname = surname
        self.birth_date = self.date(birth_date)
        self.death_date = self.date(death_date) if death_date else None
        self.gender = gender


    def date(self, date_str):
        if date_str:
            formats = ['%d.%m.%Y', '%m %d %Y', '%d/%m/%Y', '%m-%d-%Y']
            for f in formats:
                try:
                    return datetime.strptime(date_str, f).date()
                except ValueError:
                    pass
            raise ValueError("Невірний формат даних")


    def calculate_age(self, today=None):
        today = today or datetime.now().date()
        birth_date = self.birth_date
        death_date = self.death_date

        if birth_date is None:
            return None

        if death_date and death_date <= today:
            return (death_date - birth_date).days // 365
        else:
            return (today - birth_date).days // 365 if birth_date else None

    def __str__(self):
        return f"{self.name} {self.second_name} {self.surname}, {self.birth_date} - {self.death_date} ({Person.calculate_age(self)} років), {self.gender}"


class Database:


    def __init__(self):
        self.people = []


    def add_person(self, person):
        self.people.append(person)


    def search_people(self, query):
        results = []
        for person in self.people:
            if query.lower() in person.__str__().lower():
                results.append(person)
        return results


    def save_to_file(self, filename):
        with open(filename, 'a', encoding='utf-8') as file:
            for person in self.people:
                file.write(f"{person.__str__()}\n")


    def load_from_file(self, filename):
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                for line in file:
                    data = [item.strip() for item in line.strip().split(',')]
                    if len(data) < 3:
                        print(f"Помилка у форматі рядка (недостатньо даних): {line}")
                        continue

                    name, second_name, surname = data[:3]
                    birth_date, death_date, gender = data[3:6] if len(data) >= 6 else [None, None, None]

                    try:
                        person = Person(name, second_name, surname, birth_date, death_date, gender)
                        self.people.append(person)
                    except Exception as e:
                        print(f"Помилка при створенні об'єкта Person для рядка: {line}")
                        print(f"Ісключення: {e}")
        except FileNotFoundError:
            self.people = []


database = Database()
database.load_from_file("Список1.txt")

while True:
    print("\nМеню:")
    print("1. Ввести нові дані про людину")
    print("2. Провести пошук")
    print("3. Вийти")

    choice = input("Виберіть опцію: ")

    if choice == "1":
        name = input("Ім'я: ")
        second_name = input("По-батькові (Enter для пропуску): ")
        surname = input("Прізвище (Enter для пропуску): ")
        birth_date = input("Дата народження (у форматі dd.mm.yyyy): ")
        death_date = input("Дата смерті (Enter, якщо живий, або у форматі dd.mm.yyyy): ")
        gender = input("Стать (m/f): ")

        person = Person(name, second_name, surname, birth_date, death_date, gender)
        database.add_person(person)

    elif choice == "2":
        query = input("Введіть запит для пошуку: ")
        results = database.search_people(query)

        if results:
            for idx, person in enumerate(results, 1):
                print(f"{idx}. {person}")
        else:
            print("Збігів не знайдено.")

    elif choice == "3":
        filename = input("Введіть ім'я файлу для збереження (Enter для пропуску): ")
        if filename:
            database.save_to_file(filename)
            print(f"Дані збережено у файл {filename}")

        break
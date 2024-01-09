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

        if death_date and death_date <= today:
            return (death_date - birth_date).days // 365
        else:
            return (today - birth_date).days // 365

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
        with open(filename, 'w') as file:
            for person in self.people:
                file.write(f"{person.__str__()}\n")

    def load_from_file(self, filename):
        with open(filename, 'r') as file:
            for line in file:
                data = line.strip().split()
                person = Person(*data)
                self.people.append(person)


database = Database()

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

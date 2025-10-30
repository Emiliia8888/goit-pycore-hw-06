from collections import UserDict
from typing import List

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    # реалізація класу
		pass


def check_number(number: str):
    if len(number) != 10 or not number.isdigit():
        raise Exception("Invalid number")


class Phone(Field):
    def __init__(self, number):
        check_number(number)
        super().__init__(number)

    def update(self, number):
        check_number(number)
        self.value = number


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones: List[Phone] = []

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

    def add_phone(self, number):
        self.phones.append(Phone(number))

    def find_phone(self, number) -> Phone | None:
        for p in self.phones:
            if p.value == number:
                return p
        pass

    def edit_phone(self, number, new_phone):
        phone = self.find_phone(number)
        if phone:
            phone.update(new_phone)
        pass

    def remove_phone(self, number):
        phone = self.find_phone(number)
        if phone:
            self.phones.remove(phone)


class AddressBook(UserDict):

    def add_record(self, record: Record):
        self[record.name.value] = record

    def find(self, search) -> Record | None:
        for name, record in self.data.items():
            if name == search:
                return record
        pass

    def delete(self, param):
        deleted = self.data.pop(param, None)
        print(f"Deleted: {deleted}")


if __name__ == "__main__":
    # Створення нової адресної книги
    book = AddressBook()

    # Створення запису для John
    john_record = Record("John")
    john_record.add_phone("1234567890")
    john_record.add_phone("5555555555")
    john_record.add_phone("7777777777")

    # Додавання запису John до адресної книги
    book.add_record(john_record)

    # Створення та додавання нового запису для Jane
    jane_record = Record("Jane")
    jane_record.add_phone("9876543210")
    book.add_record(jane_record)

    # Виведення всіх записів у книзі
    for name, record in book.data.items():
        print(record)

    # Знаходження та редагування телефону для John
    john = book.find("John")
    john.edit_phone("1234567890", "1112223333")
    john.remove_phone("7777777777")

    print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

    # Пошук конкретного телефону у записі John
    found_phone = john.find_phone("5555555555")
    print(f"{john.name}: {found_phone}")  # Виведення: 5555555555

    # Видалення запису Jane
    book.delete("Jane")

    print("--------------------")
    for name, record in book.data.items():
        print(record)

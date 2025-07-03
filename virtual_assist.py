from collections import UserDict


class Filed:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Filed):
    pass


class Phone(Filed):
    def __init__(self, value):
        if not (isinstance(value, str) and value.isdigit() and len(value) == 10):
            raise ValueError("Phone number must be 10 digits.")
        super().__init__(value)


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone_number: str):
        phone = Phone(phone_number)
        self.phones.append(phone)

    def remove_phone(self, phone_number: str):
        self.phones = [p for p in self.phones if p.value != phone_number]

    def edit_phone(self, old_number: str, new_number: str):
        new_number_obj = Phone(new_number)
        for i, phone in enumerate(self.phones):
            if phone.value == old_number:
                self.phones[i] = new_number_obj
                return
        raise ValueError(f"Phone number {old_number} not found in record.")

    def find_phone(self, phone_number: str):
        for phone in self.phones:
            if phone.value == phone_number:
                return phone
        return None

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"


class AddressBook(UserDict):
    def add_record(self, record: Record):
        self.data[record.name.value] = record

    def find(self, name: str):
        return self.data.get(name)

    def delete(self, name: str):
        if name in self.data:
            del self.data[name]

    def __str__(self):
        if not self.data:
            return "Address book is empty."
        return "\n".join(str(record) for record in self.data.values())


if __name__ == "__main__":
    # Створення нової адресної книги
    book = AddressBook()

    # Створення запису для John
    john_record = Record("John")
    john_record.add_phone("1234567890")
    john_record.add_phone("5555555555")

    # Додавання запису John до адресної книги
    book.add_record(john_record)

    # Створення та додавання нового запису для Jane
    jane_record = Record("Jane")
    jane_record.add_phone("9876543210")
    book.add_record(jane_record)

    # Виведення всіх записів у книзі
    print("All records in the book:")
    print(book)
    print("-" * 20)

    # Знаходження та редагування телефону для John
    john = book.find("John")
    john.edit_phone("1234567890", "1112223333")

    print("John's record after editing:")
    print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555
    print("-" * 20)

    # Пошук конкретного телефону у записі John
    found_phone = john.find_phone("5555555555")
    print(f"Found phone for {john.name.value}: {found_phone}")  # Виведення: John: 5555555555
    print("-" * 20)

    # Пошук телефону, якого немає
    not_found_phone = john.find_phone("1231231231")
    print(f"Searching for non-existent phone: {not_found_phone}")  # Виведення: None
    print("-" * 20)

    # Видалення запису Jane
    book.delete("Jane")

    print("Book after deleting Jane:")
    print(book)
    print("-" * 20)

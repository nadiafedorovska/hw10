from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    pass

class Phone(Field):
    def __init__(self, value):
        if not self.is_valid_phone(value):
            raise ValueError("Phone number must be a ten digit string of digits")
        super().__init__(value)
    def is_valid_phone(self, value):
        return value.isdigit() and len(value) == 10

   

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone_number):
        phone = Phone(phone_number)
        if phone.value not in [p.value for p in self.phones]:
            self.phones.append(phone)

    def remove_phone(self, phone):
        for phone in self.phones:
            if phone in self.phones:
                self.phones.remove(phone)

    def edit_phone(self, old_phone, new_phone):
        old_phone_obj = Phone(old_phone)
        for phone in self.phones:
            if phone.value == old_phone_obj.value:
                phone.value = new_phone
                return 
        raise ValueError(f"Phone {old_phone} not found")

    def find_phone(self, phone_number):
        for phone in self.phones:
            if phone.value == phone_number:
                return phone
        return None

class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name, None)

    def delete(self, name):
        if name in self.data:
            del self.data[name]



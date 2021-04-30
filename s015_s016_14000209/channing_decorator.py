# Decorators
def validate_phone(func):
    """Decorator to validate phone number"""

    def inner_function(*args, **kwargs):
        p: str = func(*args, **kwargs)
        phone_number = p[-10:]
        assert phone_number.isnumeric(), "Invalid phone number: numeric"
        assert len(phone_number) == 10, "Invalid phone number: len"
        assert phone_number.startswith('9'), "Invalid phone number: start"
        return p

    return inner_function


def prefix(func):
    """Add ‘+98’ prefix to phone number"""

    def inner_function(*args, **kwargs):
        phone_number: str = func(*args, **kwargs)
        phone_number = phone_number[-10:]
        return '+98' + phone_number

    return inner_function


# User class
class User:
    def __init__(self, id, name, phone):
        self.__id = id
        self.__name = name
        self.__phone = phone

    @property
    @prefix
    @validate_phone
    def phone(self):
        return self.__phone


# Calling
users = [User(1, 'Akbar', '+989123456781'),
         User(2, 'Asqar', '09123456782'),
         User(3, 'Reza', '9123456783'),
         User(4, 'Mamad', '1234'),
         User(5, 'Bagher', '0123412381'),
         ]


print(users[0].phone)
print(users[1].phone)
print(users[2].phone)
print(users[3].phone)
print(users[4].phone)
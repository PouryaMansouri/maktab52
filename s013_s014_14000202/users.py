class UserException(Exception):
    def __init__(self, msg, filed, data, *args):
        self.msg = f"in {filed=} your {data=} is {msg}"
        self.data = data
        self.filed = filed
        super().__init__(self.msg)


class User:
    def __init__(self, id, name, phone, email):
        self.id = id
        self.name = name
        self.phone = phone
        self.email = email

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        if not isinstance(id, int):
            raise UserException("invalid ID", "ID", id)
        self.__id = id

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        name_without_space = name.replace(' ', '')
        if not name_without_space.isalpha():
            raise UserException("invalid name", "NAME", name)
        self.__name = name

    @property
    def phone(self):
        return self.__phone

    @phone.setter
    def phone(self, phone):
        if not (phone.isnumeric() and phone.startswith('09')):
            raise UserException("invalid phone", "PHONE", phone)

        self.__phone = phone

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        if not (email.isascii() and email.count('@') == 1):
            raise UserException("invalid email", "EMAIL", email)
        self.__email = email


u1 = User(3, "Pourya M", "09132488545", "pourya@gmail.com" )
print(u1.id)
print(u1.name)
print(u1.phone)
print(u1.email)

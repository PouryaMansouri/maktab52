import logging

logging.basicConfig(level=logging.INFO)


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
        self.password = password

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

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, password):
        if not (len(password) >= 8 and password.isascii() and (' ' not in password)):
            raise UserException("invalid password", "PASSWORD", password)
        self.__password = password


class NormalizerError(Exception):
    ...


class EmailError(NormalizerError):
    pass


def normalize_email(email: str):
    """
    Normalize user email using RegEx
    :param email: user email
    :return: normalized and lower email address
    :raises `EmailError`
    """
    import re
    email_regex = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
    if not re.match(email_regex, email):
        raise EmailError("Invalid email")
    return email.lower()


class PhoneNumError(NormalizerError):
    phone_number: str

    def __init__(self, phone_number, *args):
        super().__init__(*args)
        self.phone_number = phone_number


def normalize_phone(phone_num: str, prefix_num='+98'):
    # Get last 10 digits of phone number (must starts with '9')
    phone_num = phone_num[-10:]
    if len(phone_num) < 10:
        raise PhoneNumError(phone_num, "Phone number Length must be >= 10 .")
    if not phone_num.isnumeric():
        raise PhoneNumError(phone_num, "Phone number is NOT numeric.")
    if not phone_num.startswith('9'):
        raise PhoneNumError(phone_num, "Phone number does NOT start with '9'.")
    return prefix_num + phone_num  # Also may raises `TypeError `


def register_user(phone, password, name, email):
    return User(id=count, phone=phone, name=name, password=password, email=email)


if __name__ == '__main__':
    count = 1
    print("USER MANAGER PROGRAM")
    print("\t 1. Register")
    print("\t 2. Login")
    print("Enter option: ")
    option = input()

    if option == '1':
        print("USER MANAGER > REGISTER")
        phone = input('>> phone: ')
        password = input('>> password: ')
        name = input('>> name: ')
        email = input('>> email: ')
        try:
            new_user = register_user(phone, email, password, name)
        except Exception as error:
            logging.error("invalid input, Registration Failed--->" + str(error.args))
            # print(error.args)
        else:
            logging.info("Registered Successfully!")
            # print("Registered Successfully!")
            with open('users.info', 'a') as f:
                f.write(str(new_user) + "\n")
            logging.info("new user add to file")


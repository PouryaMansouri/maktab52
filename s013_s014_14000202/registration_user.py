import logging
import pickle


class NormalizerError(Exception):
    pass


class EmailError(NormalizerError):
    pass


class UserException(Exception):
    def __init__(self, msg, filed, data, *args):
        self.msg = f"in {filed=} your {data=} is {msg}"
        self.data = data
        self.filed = filed
        super().__init__(self.msg)


class User:
    def __init__(self, id, name, phone, email, password):
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
        if not (password.isascii() and (' ' not in password) and len(password) >= 8):
            raise UserException('invalid password', 'password', password)
        self.__password = password


def register_user(name, password, phone, email):
    count = 0
    count += 1
    return User(id=count, name=name, phone=phone, password=password, email=email)


def main():
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
            new_user = register_user(name, password, phone, email)

        except Exception as error:
            # print(error.args)
            logging.error(error.args)
        else:
            logging.info("Registered Successfully!")
            # print("Registered Successfully!")
            with open('users.info', 'ab') as f:
                # pickled = pickle.dumps(new_user)
                # f.write(str(new_user) + "\n")
                pickle.dump(new_user, f)
                f.write(b'\n')

            logging.info("new user add to file")
    elif option == '2':
        print("USER MANAGER > LOGIN")
        phone = input('>> phone: ')
        password = input('>> password: ')
        with open('users.info', 'rb') as f:
            users_info = pickle.load(f)
            for user in users_info:
                if user.phone == phone and user.password == password:
                    print('login successfully!!!')
                    break
            else:
                logging.error('invalid password or phone!!!')


main()


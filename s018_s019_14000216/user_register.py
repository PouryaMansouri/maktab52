import argparse


class User:

    def __init__(self, id, first_name, last_name, phone, email, age, gender, type, active, *args):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.email = email
        self.age = age
        self.gender = gender
        self.type = type
        self.active = active
        self.extra = args

    def __str__(self):
        return f"""User #{self.id}:
- first_name: {self.first_name} 
- last_name: {self.last_name} 
- phone: {self.phone} 
- email: {self.email} 
- age: {self.age} 
- gender: {self.gender} 
- type: {self.type} 
- active: {self.active} 
- extra: {self.extra}
"""


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='User Registration script')
    parser.add_argument(metavar='ID', action='store', dest='id', type=int, help='User id')
    parser.add_argument(metavar='FirstName', action='store', dest='first_name', help='First name')
    parser.add_argument(metavar='LastName', action='store', dest='last_name', help='Last name')
    parser.add_argument('-p', '--phone', metavar='Phone', action='store', required=True, help='Phone number')
    parser.add_argument('-e', '--email', metavar='Email', action='store', default=None, help='Email address')
    parser.add_argument('-a', '--age', metavar='Age', action='store', type=int, default=None)
    parser.add_argument('-g', '--gender', metavar='Gender', action='store', choices=['male', 'female'])
    parser.add_argument('--admin', metavar='Admin', action='store_const', const='admin', default='user', dest='type')
    parser.add_argument('--active', action='store_true', dest='active')
    parser.add_argument('--extra', action='store', nargs='*', help='Extra arguments')
    args = parser.parse_args()
    extra = args.extra or ()
    u = User(id=args.id, first_name=args.first_name, last_name=args.last_name, phone=args.phone, email=args.email,
             age=args.age, gender=args.gender, type=args.type, active=args.active, *extra)
    print(u)

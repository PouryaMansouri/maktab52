class User:
    def __init__(self, id, name, phone):
        self.id = id
        self.name = name
        self.phone = phone

    def save(self):
        file_name = f'{self.id}.user'

        with open(file_name, 'w') as f:
            f.write(f'{self.id=}\n{self.name=}\n{self.phone=}')
        return file_name

    @classmethod
    def from_file(cls, file_path):
        self = User.__new__(User)

        with open(file_path, 'r') as f:
            file_content = f.read()
            exec(file_content)
        return self


u = User(1, 'akbar', '9129000111')
file_name = u.save()
print(file_name) #???

other_u = User.from_file(file_name)
print(other_u.id, other_u.name, other_u.phone) #???

file_name2 = 'akbar.user'
other_u = User.from_file(file_name2)
print(other_u.id, other_u.name, other_u.phone) #???

import pickle
import dill


class User:
    def __init__(self, id, first_name, last_name, phone):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone

    def fullname(self):
        return f"{self.first_name} {self.last_name}"

    def __repr__(self):
        return f"{self.id}: {self.first_name} {self.last_name} <{self.phone}>"


file_pickle = "./users.pickled"
file_out1 = "./output-q-5-1.txt"
file_out2 = "./output-q-5-2.txt"
file_out3 = "./output-q-5-3.txt"

with open(file_pickle, 'rb') as f:
    unpickle = pickle.load(f)

sorted_by_id = sorted(unpickle, key=lambda x: x.id)
with open(file_out1, 'w') as f:
    for _ in sorted_by_id:
        f.write(str(_) + '\n')

sorted_by_phone = sorted(unpickle, key=lambda x: x.phone)
with open(file_out2, 'w') as f:
    result = list(filter(lambda user: str(user.phone).startswith('0919'), sorted_by_phone))
    for _ in result:
        f.write(str(_) + "\n")

list_user = dict()
for _ in unpickle:
    list_user[_.fullname()] = _

with open(file_out3, 'wb') as f:
    dill.dump(list_user, f)

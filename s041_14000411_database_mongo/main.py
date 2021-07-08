import pymongo
from icecream import ic

client = pymongo.MongoClient("localhost", 27017)
db = client.lab


# db.patient_doc.insert_one({
#     "first_name": "Hamid",
#     "last_name": "fekri",
#     "phone": "09123456789",
#     "national_code": "123456789",
#     "tests": [
#         {
#             "name": "blood test",
#             "price": 20000
#         }
#
#     ]
# })


# #
# db.test_doc.insert_one(
#     {
#         "name": "corona_test",
#         "price": 50000,
#     }
# )


# db.employee.insert_one({
#     "first_name": "mohammad",
#     "last_name": "ayazade",
#     "phone": "099123455667",
#     "national_code": "123456789",
#     "role": "doctor"
# })
#

def read_test():
    list_test = []
    for _ in db.test_doc.find():
        list_test.append(_)
    return list_test


def patient_doc():
    list_test = []
    for _ in db.patient_doc.find():
        list_test.append(_)
    return list_test


def create_employee():
    data = {}
    fields = ["first_name",
              "last_name",
              "phone",
              "national_code",
              "role"]
    for i in fields:
        data[i] = input(f"{i}: ")
    _id = db.employee.insert_one(data)
    return _id


# print(create_employee())


def create_patients_doc():
    fields = [
        "first_name",
        "last_name",
        "phone",
        "national_code",
        "tests"
    ]
    data = {}
    for field in fields:
        if field == "tests":
            list_tests = read_test()
            test_array = []
            for test in list_tests:
                print(test['name'])
                ans = input("want?(y/n) ")
                if ans.lower() == 'y':
                    test_array.append(test)
            data[field] = test_array
        else:
            data[field] = input(f"{field}: ")

    _id = db.patient_doc.insert_one(data)
    return _id


ic(read_test())
ic(patient_doc())

ic(list(db.patient_doc.aggregate([
    {'$group': {'_id': "$first_name", 'totol': {'$sum': 1}}}
])))

pipeline = [
{'$group': {'_id': "$national_code", 'totol': {'$sum': 1}}}
]
ic(db.command('aggregate', 'things', pipeline=pipeline, explain=True))

ic(db.patient_doc.distinct("first_name"))

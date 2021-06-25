import pymongo
from bson import ObjectId  # Independent BSON codec for Python that doesn’t depend on MongoDB.
import json

client = pymongo.MongoClient("localhost", 27017)
db = client.phonebook
id = db.contact.insert_one({"first_name": "mohamad", "last_name": "ayazadeh",
                            "phone": [{"title": "work", "number": "123456789"},
                                      {"title": "home", "number": "987654321"}]}).inserted_id


def read_all():
    for _ in db.contact.find():
        print(_)


def update_phone(db, user_id, new_phone, title="work"):
    for contact in db.contact.find({"_id": user_id}):
        print(contact)
        phone_list: list = contact["phone"]
        for i in range(len(phone_list)):
            if title in phone_list[i]:
                if phone_list[i]["title"] == title:
                    index = i
                    filter = {"_id": user_id}
                    newvalues = {"$set": {f"phone.{index}.number": new_phone}}
                    db.contact.update_one(filter, newvalues)


def remove(user_id):
    filter = {"first_name": "mohamad"}
    db.contact.delete_many(filter)


print("all_data")
read_all()

print("update")
user_id = ObjectId('60d4789cc507707bc58ff7a0')  # Independent BSON codec for Python that doesn’t depend on MongoDB.
new_phone = "111111111111"
update_phone(db, user_id, new_phone, title="home")

print("remove_user")
remove(id)
print("-------------")
print("all_data")
read_all()

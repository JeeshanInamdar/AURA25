from .models import participants
from bson.objectid import ObjectId

def insert(name,email,ph_no):

    participants.insert_one({"name":name,"email":email,"ph_no":ph_no})

def find_id():
    for data in participants.find().sort([('_id', -1)]).limit(1):
        return data['_id']

def find_details(id):
    data=participants.find_one({'_id':ObjectId(id)})
    return data

def find_email(id):
    data = participants.find_one({'_id':ObjectId(id)})
    return data['email']


def find_id_using_ph_no(number):
    data=participants.find_one({'ph_no':number})
    print(f"ID: {data['_id']}")

from bson.objectid import ObjectId
from datetime import datetime
from .models import entry

def insert(_id,name):
    date=datetime.now().strftime("%d/%m/%y")
    time = datetime.now().strftime("%H:%M")
    entry.insert_one({'_id':_id,'name':name,'date':date,'time':time})

def find_details(id):
    data=entry.find_one({'_id':ObjectId(id)})
    return data

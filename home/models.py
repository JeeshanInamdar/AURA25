from django.db import models
from mongo_connection import db
from datetime import datetime

# Create your models here.
date=datetime.now().strftime("%d/%m/%y")
entry=db[f'{date}_entries']
participants=db.participants
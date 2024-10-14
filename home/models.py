from django.db import models
from mongo_connection import db
from datetime import datetime

# Create your models here.
date=datetime.now().strftime("%d/%m/%y")
entry=db[f'{date}_entries']
participants=db.participants


class QRCodeScan(models.Model):
    scanned_data = models.TextField()
    scanned_at = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return f"Scanned at {self.scanned_at}"
from django.db import models
from django.db.models.fields import CharField,TextField,DateField
from django.db.models.fields.files import  ImageField
import datetime

class Post(models.Model):
    title=CharField(max_length=100)
    description=TextField(max_length=250)
    image=ImageField(upload_to='blog_app/images')
    date=DateField(datetime.date.today)

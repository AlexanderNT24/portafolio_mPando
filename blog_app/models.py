from django.db import models
from django.db.models.fields import CharField,TextField,DateField
from django.db.models.fields.files import  ImageField
import datetime

class Post(models.Model):
    title=CharField(max_length=100)
    description=TextField(max_length=1000)
    image=ImageField(upload_to='blog_app/images')
    start_date=DateField(datetime.date.today,null=True)
    end_date=DateField(datetime.date.today,null=True)

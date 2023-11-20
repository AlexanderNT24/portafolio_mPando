from django.db import models
from django.db.models.fields import CharField, TextField, DateField
from django.db.models.fields.files import ImageField

import datetime

class Post(models.Model):
    title = CharField(max_length=100)
    description = TextField(max_length=10000, blank=True)
    image = ImageField(upload_to='blog_app/images')
    pdf_file = models.FileField(upload_to='blog_app/pdfs', null=True, blank=True)
    start_date = DateField(default=datetime.date.today, null=True, blank=True)
    end_date = DateField(default=datetime.date.today, null=True, blank=True)

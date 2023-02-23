from django.db import models
from django.db.models.fields import CharField,URLField,DateField
from django.db.models.fields.files import  ImageField

class Exhibition(models.Model):
    title=CharField(max_length=100)
    ubication=CharField(null=True,max_length=150)
    city=CharField(null=True,max_length=250)
    date=DateField(null=True)
    description=CharField(null=True,max_length=250)
    image=ImageField(upload_to='portfolio_app/images')

class Exhibition_View(models.Model):
    exhibition = models.ForeignKey(Exhibition, on_delete=models.CASCADE)
    title=CharField(max_length=100)
    description=CharField(max_length=250)
    image=ImageField(upload_to='portfolio_app/images')
    
from django.db import models
from django.db.models.fields import CharField,URLField,DateField,TextField,BooleanField
from django.db.models.fields.files import  ImageField

class Exhibition(models.Model):
    title = CharField(max_length=100)
    ubication = CharField(null=True, max_length=150, blank=True)
    city = CharField(null=True, max_length=250, blank=True)
    date = DateField(null=True)
    description = TextField(max_length=10000)
    image = ImageField(upload_to='portfolio_app/images')
    video_url = URLField(blank=True, null=True)
    password = CharField(null=True, max_length=250, blank=True)
    hidden = BooleanField(default=False)

class Exhibition_View(models.Model):
    exhibition = models.ForeignKey(Exhibition, on_delete=models.CASCADE)
    title=CharField(max_length=100,blank=True)
    description=TextField(max_length=250,blank=True)
    image=ImageField(upload_to='portfolio_app/images')
    
from django.db import models

class Exhibition(models.Model):
    title = models.CharField(max_length=100)
    ubication = models.CharField(null=True, max_length=150, blank=True)
    city = models.CharField(null=True, max_length=250, blank=True)
    date = models.DateField(null=True)
    description = models.TextField(max_length=10000)
    image = models.ImageField(upload_to='portfolio_app/images')
    video_url = models.URLField(blank=True, null=True)
    password = models.CharField(null=True, max_length=250, blank=True)
    hidden = models.BooleanField(default=False)

class Exhibition_View(models.Model):
    exhibition = models.ForeignKey(Exhibition, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, blank=True)
    description = models.TextField(max_length=250, blank=True)
    image = models.ImageField(upload_to='portfolio_app/images')
    order = models.PositiveIntegerField(default=0, help_text='Order for display')

    class Meta:
        ordering = ['order']

class BiographyType(models.Model):
    name = models.CharField(max_length=100)

class Biography(models.Model):
    biography_type = models.ForeignKey(BiographyType, on_delete=models.CASCADE)  
    date = models.DateField()
    description = models.TextField(max_length=10000)

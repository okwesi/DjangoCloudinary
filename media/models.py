from django.db import models

class Media(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/', blank=True)

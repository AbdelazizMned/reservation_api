from django.db import models

class books(models.Model):
  title = models.CharField(max_length=200)
  author = models.CharField(max_length=200)
  image = models.ImageField(upload_to='images', null=True)
  available = models.BooleanField(default=True)
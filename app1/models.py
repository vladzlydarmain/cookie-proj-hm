from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.TextField(max_length=30)
    cost = models.TextField(max_length=20)
    image = models.ImageField(upload_to='media')
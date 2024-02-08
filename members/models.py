from django.db import models

# Create your models here.
class Usuario(models.Model):
    email = models.EmailField(max_length=50)
    senha = models.CharField(max_length=50)

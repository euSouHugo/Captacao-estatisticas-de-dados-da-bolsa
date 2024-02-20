from django.db import models

# Create your models here.
class Usuario(models.Model): 
    email = models.EmailField(max_length=50) #templates pré prontos do Django.
    senha = models.CharField(max_length=50)

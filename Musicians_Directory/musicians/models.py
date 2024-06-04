from django.db import models

class Musician(models.Model):
    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)
    email = models.EmailField()
    phone = models.CharField(max_length=12)
    instrumetType = models.CharField(max_length=30)
    
    def __str__(self) -> str:
        return f'{self.firstName}'
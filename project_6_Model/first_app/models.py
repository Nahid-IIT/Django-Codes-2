from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=20)
    roll = models.IntegerField(primary_key=True)
    address  = models.TextField()
    father_name = models.TextField(default="Rahim")
    
    def __str__(self) -> str:
        return f'{self.roll}\t{self.name}\t{self.father_name}\t{self.address}'
from django.db import models

# Create your models here.

class StudentModel(models.Model):
   roll =models.IntegerField(primary_key=True)
   name = models.CharField(max_length=20)
   father_name = models.CharField(max_length=20)
   address = models.TextField()
   
   def __str__(self) -> str:
      return f'{self.roll}\t {self.name}\t{self.father_name}\t{self.address}'
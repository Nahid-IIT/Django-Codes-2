from django.db import models
from musicians.models import Musician

class Album(models.Model):
    
    name = models.CharField(max_length=50)
    musician = models.ForeignKey(Musician, on_delete=models.CASCADE)
    releseDate = models.DateField()
    lst = [('1','1'), ('2','2'),('3','3'),('4', '4')]
    rating = models.CharField(max_length=10, choices=lst)
    
    def __str__(self) -> str:
        return f'{self.name}'
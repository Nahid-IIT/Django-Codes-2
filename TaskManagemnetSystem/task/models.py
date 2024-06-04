from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    is_completed = models.BooleanField(default=False)
    assignDate = models.DateField()
    
    def __str__(self) -> str:
        return f"{self.title}\t{self.assignDate}"
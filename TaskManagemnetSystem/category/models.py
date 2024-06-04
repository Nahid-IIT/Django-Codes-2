from django.db import models
from task.models import Task

class Category(models.Model):
    name = models.CharField(max_length=50)
    task = models.ManyToManyField(Task)
    def __str__(self) -> str:
        return f"{self.name}"
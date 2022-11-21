from django.db import models

from datetime import datetime

# Create your models here.


class Note(models.Model):
    name = models.CharField(max_length=40)
    content = models.TextField(max_length=280)
    created_at = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.name

from django.db import models
from datetime import datetime as dt

# Create your models here.


class Agent(models.Model):

    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    phone = models.CharField(max_length=11)
    email = models.CharField(max_length=100)
    is_mvp = models.BooleanField(default=False)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d')
    hire_date = models.DateTimeField(default=dt.now, blank=True)

    def __str__(self):
        return self.name


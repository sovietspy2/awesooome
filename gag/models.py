from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone
import datetime


class User(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Post(models.Model):
    post_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date posted')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    deleted =  models.CharField(max_length=3, default='no')
    likes = models.IntegerField(default = 0)

    def __str__(self):
        return self.post_text

    def is_it_deleted(self):
        return self.deleted



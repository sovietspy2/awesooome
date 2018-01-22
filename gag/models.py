from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone
import datetime
from django.contrib.auth.models import User

from django.core.files.storage import FileSystemStorage

fs = FileSystemStorage(location='/var/www/html')


class Post(models.Model):
    post_text = models.CharField(max_length=200)
    #pub_date = models.DateTimeField('date posted')
    pub_date = timezone.now()
    #author = models.ForeignKey(User, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    deleted = models.CharField(max_length=3, default='no')
    likes = models.IntegerField(default = 0)
    image = models.ImageField(storage=fs)

    def __str__(self):
        return self.post_text

    def is_it_deleted(self):
        return self.deleted



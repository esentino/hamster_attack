from django.contrib.auth.models import User
from django.db import models


class Picture(models.Model):
    path = models.ImageField()
    creation_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

from django.db import models
# from django.contrib.auth.models import AbstractUser
# DONE: may have to come back to get_user_model
from django.contrib.auth import get_user_model

class Thing(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField(default='')
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return self.name

from django.db import models
from django.contrib.auth import get_user_model


class Movie(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField()
    rating = models.IntegerField(default = 0)
    reviewer = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return self.name


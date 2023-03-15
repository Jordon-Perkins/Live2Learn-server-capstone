from django.db import models
from .ThisClass import ThisClass

class Tag (models.Model):
    tag = models.CharField(max_length=55)
    this_class = models.ForeignKey(ThisClass, on_delete=models.CASCADE)
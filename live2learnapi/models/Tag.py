from django.db import models
from .Learner import Learner

class Tag (models.Model):
    tag = models.CharField(max_length=55)
    learner = models.OneToOneField(Learner, on_delete=models.CASCADE)
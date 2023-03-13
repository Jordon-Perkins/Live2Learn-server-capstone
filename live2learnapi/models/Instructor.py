from django.db import models
from .Learner import Learner
from .ThisClass import ThisClass

class Instuctor (models.Model):
    learner = models.ForeignKey(Learner, on_delete=models.CASCADE, related_name='instructor')
    this_class = models.ForeignKey(ThisClass, on_delete=models.CASCADE, related_name='instructor_class')
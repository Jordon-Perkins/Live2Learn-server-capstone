from django.db import models
from .Learner import Learner
from .ThisClass import ThisClass

class Student (models.Model):
    learner = models.ForeignKey(Learner, on_delete=models.CASCADE, related_name='student')
    this_class = models.ForeignKey(ThisClass, on_delete=models.CASCADE, related_name='student_class')
from django.db import models
from .ThisClass import ThisClass

class Instructor (models.Model):
    user = models.ForeignKey("live2learnapi.UserProfile", on_delete=models.CASCADE, related_name='instructor')
    this_class = models.ForeignKey(ThisClass, on_delete=models.CASCADE, related_name='instructor_class')
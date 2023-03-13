from django.db import models

class Student (models.Model):
    user = models.ForeignKey("live2learnapi.UserProfile", on_delete=models.CASCADE, related_name='student')
    this_class = models.ForeignKey("live2learnapi.ThisClass", on_delete=models.CASCADE, related_name='student_class')
from django.db import models
from .Skill import Skill


class ThisClass(models.Model):
    instructor = models.ManyToManyField("live2learnapi.UserProfile", through='Instructor', related_name='class_instructor')
    description = models.CharField(max_length=200)
    date = models.DateField(auto_now=False, null=True)
    time = models.TimeField(auto_now=False, null=True)
    students = models.ManyToManyField("live2learnapi.UserProfile", through='Student', related_name='class_students')
    title = models.CharField(max_length=20)
    skill = models.ForeignKey(Skill, on_delete=models.SET_NULL, null=True)

    @property
    def joined(self):
        return self.__joined

    @joined.setter
    def joined(self, value):
        self.__joined = value

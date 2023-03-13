from django.db import models
from .Learner import Learner
from .Skill import Skill
from .Instructor import Instructor
from .Student import Student


class ThisClass (models.Model):
    instructor = models.ManyToManyField(Instructor, through='Instructor', related_name='class_instructor')
    description = models.CharField(max_length=200)
    date = models.DateField(auto_now=False, null=True)
    time = models.TimeField(auto_now=False, null=True)
    students = models.ManyToManyField(Student, through='Student', related_name='class_students')
    title = models.CharField(max_length=20)
    skill = models.ForeignKey(Skill, on_delete=models.SET_NULL, null=True)

    @property
    def joined(self):
        return self.__joined

    @joined.setter
    def joined(self, value):
        self.__joined = value

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User


class UserProfile(AbstractUser):

    bio = models.CharField(max_length=50)

    classes_teaching = models.ManyToManyField("live2learnapi.ThisClass", through='Instructor', related_name='class_teaching')
    classes_attending = models.ManyToManyField("live2learnapi.ThisClass", through='Student', related_name='class_attending')

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

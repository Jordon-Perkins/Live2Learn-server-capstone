from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=50)
    classes_teaching = models.ManyToManyField("live2learnapi.ThisClass", through='Instructor', related_name='class_teaching')
    classes_attending = models.ManyToManyField("live2learnapi.ThisClass", through='Student', related_name='class_attending')

    @property
    def full_name(self):
        return f'{self.user.first_name} {self.user.last_name}'
from django.db import models

class Skill (models.Model):
    skill_level= models.CharField(max_length=30)
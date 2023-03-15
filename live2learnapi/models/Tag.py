from django.db import models

class Tag (models.Model):
    tag = models.CharField(max_length=55)
    this_class = models.ForeignKey("live2learnapi.ThisClass", on_delete=models.CASCADE)
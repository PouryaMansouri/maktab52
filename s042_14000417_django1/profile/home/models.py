from django.db import models


# Create your models here.

class home(models.Model):
    q = models.CharField(max_length=250)

from django.db import models
from core.models import TimeStampedModel


# Create your models here.


class Category(TimeStampedModel):
    """
    create category for items
    """

    name = models.CharField(max_length=50)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}"


class Item(TimeStampedModel):
    """
    item model
    """
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100, null=True)
    price = models

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


class Price(TimeStampedModel):
    """
    price table
    """
    start_date = models.DateField()
    amount = models.IntegerField()

    def __str__(self):
        return f"price: {self.amount} |SD: {self.start_date}"


class Item(TimeStampedModel):
    """
    item model
    """
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.ForeignKey(Price, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}"

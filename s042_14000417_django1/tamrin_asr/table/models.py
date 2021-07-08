from django.db import models
from core.models import TimeStampedModel

STATUS = {
    ('FR', 'free'),
    ('FU', 'full'),
    ('RE', 'reserve')

}


# Create your models here.

class Table(TimeStampedModel):
    """
    table model
    """

    name = models.CharField(max_length=30)
    capacity = models.IntegerField()
    status = models.CharField(max_length=10, choices=STATUS, default='FR')

    # status = Choices(STATUS_ORDER)

    def __str__(self):
        return f"{self.name} | {self.capacity} sits | status: {self.status} "

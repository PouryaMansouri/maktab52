from django.db import models

# Create your models here.
STATUS = {
    ('FR', 'free'),
    ('FU', 'full'),
    ('RE', 'reserve')

}


class Table(models.Model):
    """
    table model
    """

    name = models.CharField(max_length=30)
    capacity = models.IntegerField()
    status = models.CharField(max_length=10, choices=STATUS, default='FR')

    def __str__(self):
        return f"{self.name}|{self.capacity} sits|{self.status}"

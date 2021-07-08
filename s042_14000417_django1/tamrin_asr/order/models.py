from django.db import models
from core.models import TimeStampedModel
from menu.models import Item
from table.models import Table

# Create your models here.
STATUS_ORDER = {
    ('P', 'Pending'),
    ('A', 'Accept'),
    ('R', 'Reject')
}

STATUS_RECEIPT = {
    ('N', 'Not Pay'),
    ('P', 'Pay')
}


class Order(TimeStampedModel):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    table = models.ForeignKey(Table, on_delete=models.SET_NULL, blank=True, null=True)
    count = models.IntegerField()
    receipt = models.ForeignKey('Receipt', on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=STATUS_ORDER, default='P')

    def __str__(self):
        return f"{self.id}|{self.item}"


class Receipt(TimeStampedModel):
    status = models.CharField(max_length=10, choices=STATUS_RECEIPT, default='N')

    @property
    def orders(self):
        return list(Order.objects.filter(receipt=self))

    @property
    def final_price(self):
        orders_price = list(map(lambda x: x.item.price.amount, list(Order.objects.filter(receipt=self))))
        return sum(orders_price)

    def __str__(self):
        return f"{self.orders} | price: {self.final_price}$ "

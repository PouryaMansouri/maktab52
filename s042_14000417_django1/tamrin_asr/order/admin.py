from django.contrib import admin
from .models import Order, Receipt


# Register your models here.
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'item', 'table', 'count', 'receipt', 'status', 'created', 'modified')


class ReceiptAdmin(admin.ModelAdmin):
    list_display = ('id', 'orders','status', 'final_price', 'created', 'modified')


admin.site.register(Order, OrderAdmin)
admin.site.register(Receipt, ReceiptAdmin)

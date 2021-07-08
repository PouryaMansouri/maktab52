from django.contrib import admin

# Register your models here.
from menu.models import Category, Price, Item


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent', 'created', 'modified')


class PriceAdmin(admin.ModelAdmin):
    list_display = ('id', 'start_date', 'amount', 'created', 'modified')


class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price', 'created', 'modified')


admin.site.register(Category, CategoryAdmin)
admin.site.register(Price, PriceAdmin)
admin.site.register(Item, ItemAdmin)

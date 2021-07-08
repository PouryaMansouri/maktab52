from django.contrib import admin

# Register your models here.

from .models import Table


class TableAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', 'capacity', 'created', 'modified')


admin.site.register(Table, TableAdmin)

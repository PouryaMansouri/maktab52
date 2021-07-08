from django.contrib import admin

# Register your models here.
from menu.models import Category


class CategoryAdmin(admin.ModelAdmin):
    list_display = ( 'name', 'parent', 'created', 'modified')


admin.site.register(Category,CategoryAdmin)

from django.shortcuts import render, get_object_or_404
from .models import Item, Category


# Create your views here.


def index(request):
    items = Item.objects.all()
    categories = Category.objects.all
    context = {
        'items': items,
        'categories': categories
    }
    return render(request, template_name='menu/index.html', context=context)


def item_details(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    context = {
        'item': item
    }
    return render(request, template_name='menu/item/item.html', context=context)

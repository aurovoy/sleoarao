from django.shortcuts import render
from .models import Item, Photo
# Create your views here.


def index(request):
    item_data = Item.objects.all()[:10]

    context = { 'item':item_data }
    return render(request, 'gallery/index.html', context)
    
    
def itemlist(request):
    item_data = Item.objects.all()

    context = { 'item':item_data }
    return render(request, 'gallery/item.html', context)

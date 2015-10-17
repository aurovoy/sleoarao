from django.shortcuts import render
from .models import Item, Photo
# Create your views here.


def index(request):
    try:
        itemlist = Item.objects.order_by('-timestamp')[:9]

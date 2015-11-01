from django.shortcuts import render
from .models import Item, Photo
from items.imgselect import imgselect_pac, imgselect_obj
from items.imgarray import arr
# Create your views here.


def index(request):
    item_data = Item.objects.all()[:10]

    context = { 'item':item_data }
    return render(request, 'gallery/index.html', context)
    
    
def itemlist(request):
    item_data = Item.objects.all()
    itempac = imgselect_pac(item_data)

    item_list = arr(itempac)

    context = { 'item':item_list }
    return render(request, 'gallery/item.html', context)

def itemdetail(request, item_id):
    try:
        item_detail = Item.objects.get(pk=item_id)
    except Item.DoesNotExist:
        raise Http404("Item does not exist")

    item_d = imgselect_obj(item_detail)


    photos = Photo.objects.filter(
            item__pk = item_id
            )
    photo_pac = imgselect_pac(photos)

    photo_list = arr(photo_pac)

    
    context = {"item":item_d, "photos":photo_list}
    return render(request, 'gallery/item_detail.html', context)

def photodetail(request, item_id, photo_id):
    try:
        photo_detail = Photo.objects.get(pk=photo_id)
    except Photo.DoesNotExist:
        raise Http404("Photo does not exist")

    photo_d = imgselect_obj(photo_detail)


    context={"photo":photo_d}
    return render(request, 'gallery/photo_detail.html', context)

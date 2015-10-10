from django.shortcuts import render
from .models import Welcome
from django.http import Http404
# Create your views here.

def welcome(request):
    try:
        Data = Welcome.objects.order_by('-TimeStamp')[0]
        
        ImageURL = Data.Image.url    


        Title = Data.Title
        WelContent = Data.WelcomeContent

        context = { 'WelcomeTitle': Title, 'WelcomeContent': WelContent, 'ImageURL':ImageURL}
        return render(request, 'welcome/welcome.html', context)
    except:
        raise Http404('Construction have not done.')




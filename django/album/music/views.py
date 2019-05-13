from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .models import Album


# Create your views here.
def index(request):
    # return HttpResponse('Hello world!')
    album_all = Album.objects.all()
    context = {
        'album_all': album_all,
    }
    return render(request, 'music/index.html', context)

def detail(request, album_id):
    # try:
    #     album = Album.objects.get(pk=album_id)
    # except Album.DoesNotExist:
    #     raise Http404("This page is not exist")

    album = get_object_or_404(Album, pk=album_id)
    context = {
        'album': album,
    }
    return render(request, 'music/detail.html', context)
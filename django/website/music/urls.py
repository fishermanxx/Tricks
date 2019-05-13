from django.urls import path
from django.conf.urls import url
from . import views
import re


app_name = 'music'

urlpatterns = [
	## /music/
    # path('', views.index, name='index'),
    path('', views.IndexView.as_view(), name='index'),

    ## /music/id/
    # url(r'^(?P<album_id>[0-9]+)/$', views.detail, name='detail'),
    # url(r'^(\d+)/$', views.detail, name='detail'),
    # path('<int:album_id>/', views.detail, name='detail'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),

    path('album/add', views.AlbumCreate.as_view(), name='album-add')

    ## /music/id/favourite/
    # path('<int:album_id>/favourite/', views.favourite, name='favourite'),
]
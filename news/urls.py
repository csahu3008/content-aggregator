from django.urls import path,re_path
from .views import AddNews,DetailNews,ListNews,SearchResults,ContentUpdator,category,wheather,likes_add,dislikes_add
urlpatterns = [
    path('search/',SearchResults,name='search'),
    path('add/',AddNews,name='add'),
    path('',ListNews,name='list'),
    path('weather/',wheather,name='weather'),
    path('detail/<int:id>/',DetailNews,name='detail'),
    path('likes/<int:id>/',likes_add,name='like'), 
    path('dislikes/<int:id>/',dislikes_add,name='dislike'), 
    path('contents/',ContentUpdator,name='updates'),
    re_path(r'^(?P<category>[a-z]*)/$',category,name='category'),
   
]

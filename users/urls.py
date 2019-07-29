from django.urls import path
from .views import signup,Login
urlpatterns = [
    path('signup/',signup,name='signup'),
    path('login/',Login,name='login'),
]

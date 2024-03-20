from django.urls import path
from django.conf.urls import handler404
from . import views

urlpatterns = [
    path('', views.index, name='home')
]

handler404 = 'home.views.my_custom_404_view'

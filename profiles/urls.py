from django.urls import path
from . import views

app_name = 'profiles'

urlpatterns = [
    path('profile/', views.profile, name='profile'),
    path('order_history/<order_number>', views.order_history, name='order_history'),
    path('subscribe/', views.newsletter_subscribe, name='newsletter_subscribe'),
]
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='index.html'),
    path('contact/', views.contact, name='contact')
]

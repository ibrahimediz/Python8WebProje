from django.urls import path
from . import views

urlpatterns = [ 
    path('', views.gonderi_liste, name='gonderi_liste'),
]
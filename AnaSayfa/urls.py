from django.urls import path
from . import views

urlpatterns = [ 
    path('', views.anaSayfaAc, name='anaSayfa'),
]
from django.urls import path
from . import views

urlpatterns = [ 
    path('', views.yeni_form, name='yeni_iletisim_form'),
]
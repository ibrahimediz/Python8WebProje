from django.urls import path
from . import views

urlpatterns = [ 
    path('', views.yeni_form, name='yeni_iletisim_form'),
    path('/formtamam/<str:param>',views.formtamam,name='iletisim_tamam')
]
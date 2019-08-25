from django.urls import path
from . import views

urlpatterns = [ 
    path('', views.gonderi_liste, name='gonderi_liste'),
    path('yeni/', views.yeni_gonderi, name='yeni_gonderi'),
    path('detay/<int:pk>',views.detay,name='gonderi_detay'),
    path('detay/<int:pk>/duzenle',views.gonderi_duzenle,name='gonderi_duzenle')
]
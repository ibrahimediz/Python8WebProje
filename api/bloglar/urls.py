from django.urls import path
from .views import ListBloglarView

urlpatterns = [
    path('bloglar/',ListBloglarView.as_view(),name="bloglar-tum"),
]


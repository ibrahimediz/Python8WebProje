from rest_framework import generics
from .models import Bloglar
from .serializers import BlogSerializer


class ListBloglarView(generics.ListAPIView):
    queryset = Bloglar.objects.all()
    serializer_class = BlogSerializer
    

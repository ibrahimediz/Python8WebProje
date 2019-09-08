from rest_framework import serializers
from .models import Bloglar

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bloglar
        # fields = ("baslik","yazi")
        __all__ = ["baslik","yazi"]
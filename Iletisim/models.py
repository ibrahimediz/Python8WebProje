from django.db import models
from django.utils import timezone


class iletisim(models.Model):
    Adı = models.CharField(max_length=50)
    soyAdı = models.CharField(max_length=50)
    giris_zamani = models.DateTimeField(default=timezone.now)
    giris = models.TextField(null=True)

    
    def __str__(self):
        return self.Adı+self.soyAdı


from django.db import models
from django.utils import timezone


class iletisim(models.Model):
    Adı = models.CharField(max_length=50)
    soyAdı = models.CharField(max_length=50)
    email = models.EmailField(default="aa@aa.com",blank=True)
    giris_zamani = models.DateTimeField(default=timezone.now)
    giris = models.TextField(null=True)
    girisIP = models.GenericIPAddressField(null=True)
    Onay = models.BooleanField(default=False)

    
    def __str__(self):
        return self.Adı+self.soyAdı


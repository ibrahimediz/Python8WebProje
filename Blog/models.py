from django.db import models
from django.utils import timezone


class Gonderi(models.Model):
   yazar = models.ForeignKey('auth.User',on_delete=models.CASCADE)
   baslik = models.CharField(max_length=200)
   metin = models.TextField()
   olusturma_zaman = models.DateTimeField(default=timezone.now)
   yayim_zamani = models.DateTimeField(blank=True,null=True)

   def yayimla(self):
       self.yayim_zamani = timezone.now()
       self.save()

   def __str__(self):
       return self.baslik
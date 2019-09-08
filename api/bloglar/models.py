from django.db import models


class Bloglar(models.Model):
    baslik = models.CharField(max_length=255,null=False)
    yazi = models.CharField(max_length=255,null=False)


    def __str__(self):
        return self.baslik
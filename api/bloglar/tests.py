from django.urls import reverse
from rest_framework.test import APITestCase,APIClient
from rest_framework.views import status
from .models import Bloglar
from .serializers import BlogSerializer


class BaseViewTest(APITestCase):
    client = APIClient()

    @staticmethod
    def blogOlustur(baslik="",yazi=""):
        if baslik!="" and yazi != "":
            Bloglar.objects.create(baslik=baslik,yazi=yazi)


    def setUp(self):
        self.blogOlustur("deneme1","yazi deneme1 için")
        self.blogOlustur("deneme2","yazi deneme2 için")
        self.blogOlustur("deneme3","yazi deneme3 için")
        self.blogOlustur("deneme4","yazi deneme4 için")


class ButunBloglarGetir(BaseViewTest):
    def test_get_all_bloglar(self):
        response = self.client.get(reverse("bloglar-tum",kwargs={"version":"v1"}))

        beklenen = Bloglar.objects.all()
        serializer = BlogSerializer(beklenen,many=True)
        self.assertEqual(response.data,serializer.data)
        self.assertEqual(response.status_code,status.HTTP_200_OK)

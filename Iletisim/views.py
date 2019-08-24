from django.shortcuts import render
from .forms import iletisimForm
# Create your views here.
def yeni_form(request):
    form = iletisimForm()
    return render(request, 'Iletisim/yeni_form.html', {'form': form})
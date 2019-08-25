from django.shortcuts import render,redirect
from .forms import iletisimForm
from django.http import HttpRequest  
# Create your views here.
def yeni_form(request):
    if request.method == "POST":
        form = iletisimForm(request.POST)
        if form.is_valid():
            ileti = form.save(commit=False)
            # client_address = request.META['HTTP_X_FORWARDED_FOR']
            # ileti.girisIP = client_address
            ileti.save()
            return redirect('iletisim_tamam',param="iletisim")
    else:
        form = iletisimForm()
    return render(request, 'Iletisim/yeni_form.html', {'form': form})


def formtamam(request,param):
    return render(request,'Iletisim/tamam.html',{'mesaj':param})
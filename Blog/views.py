from django.shortcuts import render,redirect,get_object_or_404
from .models import Gonderi
from .forms import GonderiForm
from django.contrib.auth.models import User

def gonderi_liste(request):
    Gonderiler = Gonderi.objects.all()
    return render(request, 'Blog/gonderi_list.html', {"gonderis":Gonderiler})

# def yeni_gonderi(request):
#     form = GonderiForm()
#     return render(request,'Blog/yeni_gonderi.html',{'form':form})

def detay(request,pk):
    gonderi =  Gonderi.objects.get(pk=pk)
    return render(request,'Blog/detay.html',{'gonderi':gonderi})


def yeni_gonderi(request):
    if request.method == "POST":
        forms = GonderiForm(request.POST)
        if forms.is_valid():
            gonderi = forms.save(commit=False)
            ben = User.objects.get(username="admin")
            gonderi.yazar = ben
            gonderi.save()
            return redirect('gonderi_detay',pk = gonderi.pk)
    else:
        forms = GonderiForm()
    return render(request,'Blog/yeni_gonderi.html',{'form':forms})


def gonderi_duzenle(request, pk):
    gonderi = get_object_or_404(Gonderi,pk=pk)
    if request.method == "POST":
        forms = GonderiForm(request.POST,instance = gonderi)
        if forms.is_valid():
            gonderi = forms.save(commit=False)
            ben = User.objects.get(username="admin")
            gonderi.yazar = ben
            gonderi.save()
            return redirect('gonderi_detay',pk = gonderi.pk)
    else:
        form = GonderiForm(instance=gonderi)
    return render(request,'Blog/yeni_gonderi.html',{'form':form})
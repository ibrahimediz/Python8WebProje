from django.shortcuts import render

def anaSayfaAc(request):
    return render(request, 'index.html', {})

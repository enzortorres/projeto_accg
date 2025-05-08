from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def adotar(request):
    return render(request, 'adotar.html')

def apadrinhamento(request):
    return render(request, 'apadrinhamento.html')
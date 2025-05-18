from django.shortcuts import render
from .models import Animal

# Create your views here.
def index(request):
    context = {
        'banner_title': 'A adoção muda duas vidas: a deles e a sua.',
        'banner_subtitle': 'Um novo começo para ambos',
        'banner_imagem': 'global/src/images/banner-home.png',
        'banner_button_text': 'Adotar',
    }
    
    return render(request, 'index.html', context=context)

def adotar(request):
    context = {
        'banner_title': 'Formulário de Adoção.',
        'banner_subtitle': 'Quer adotar um novo amigo?',
        'banner_imagem': 'global/src/images/banner-adotar.png',
    }
    
    return render(request, 'adotar.html', context=context)

def doacao(request):
    context = {
        'banner_title': 'Doações',
        'banner_subtitle': 'Com um gesto simples, você transforma vidas.',
        'banner_imagem': 'global/src/images/banner-doar.png',
    }
    
    return render(request, 'doacao.html', context=context)

def apadrinhamento(request):
    context = {
        'banner_title': 'Apadrinhar',
        'banner_subtitle': 'Com um gesto simples, você transforma vidas.',
        'banner_imagem': 'global/src/images/banner-apadrinhar.png',
    }
    
    return render(request, 'apadrinhamento.html', context=context)

def animais(request):
    animais = Animal.objects.all()
    
    context = {
        'banner_title': 'Animais para adoção',
        'banner_subtitle': 'Todos os animais merecem um lar cheio de amor e carinho.',
        'banner_imagem': 'global/src/images/banner-animais.png',
        'animais': animais,
    }
    
    return render(request, 'animais.html', context=context)

def sobre(request):
    context = {
        'banner_title': 'Conheça a ONG',
        'banner_subtitle': 'Nossa história até agora...',
        'banner_imagem': 'global/src/images/banner-sobre-nos.png',
    }
    return render(request, 'sobre.html',context=context)




from django.shortcuts import get_object_or_404, render
from django.db.models import Q
from django.core.paginator import Paginator

from datetime import date, timedelta

from ..models import Animal

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
    hoje = date.today()
    animais = Animal.objects.filter(disponivel=True)
    filtros = request.GET.get('filtros')

    if filtros:
        filtros = filtros.split(',')

        tipo_query = Q()
        porte_query = Q()
        sexo_query = Q()
        idade_query = Q()

        for f in filtros:
            if f in ['cachorro', 'gato']:
                tipo_query |= Q(tipo=f)
            elif f in ['pequeno', 'medio', 'grande']:
                porte_query |= Q(porte=f)
            elif f in ['macho', 'femea']:
                sexo_query |= Q(sexo=f)
            elif f in ['menos1ano', '1a3anos', '4a6anos', '7oumais']:
                if f == 'menos1ano':
                    data_limite = hoje - timedelta(days=365)
                    idade_query |= Q(data_nascimento__gte=data_limite)
                elif f == '1a3anos':
                    idade_max = hoje - timedelta(days=365)
                    idade_min = hoje - timedelta(days=365*3)
                    idade_query |= Q(data_nascimento__range=(idade_min, idade_max))
                elif f == '4a6anos':
                    idade_max = hoje - timedelta(days=365*3)
                    idade_min = hoje - timedelta(days=365*6)
                    idade_query |= Q(data_nascimento__range=(idade_min, idade_max))
                elif f == '7oumais':
                    data_limite = hoje - timedelta(days=365*7)
                    idade_query |= Q(data_nascimento__lte=data_limite)

        animais = animais.filter(tipo_query & porte_query & sexo_query & idade_query)

        page_obj = animais 
        total_pages = 1
    else:
        paginator = Paginator(animais, 8)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        total_pages = paginator.num_pages

    context = {
        'page_obj': page_obj,
        'total_pages': total_pages,
        'filtros': filtros or '',
    }

    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        return render(request, 'includes/animal_cards.html', context)

    context.update({
        'banner_title': 'Animais para adoção',
        'banner_subtitle': 'Todos os animais merecem um lar cheio de amor e carinho.',
        'banner_imagem': 'global/src/images/banner-animais.png',
    })

    return render(request, 'animais.html', context)


def animal(request, animal_id):
    single_animal = get_object_or_404(
        Animal,
        pk=animal_id,
        disponivel=True,
    )

    fotos = single_animal.fotos.all() #type:ignore

    context = {
        'animal': single_animal,
        'fotos': fotos,
    }

    return render(request, 'unique_animal.html', context)

def sobre(request):
    context = {
        'banner_title': 'Conheça a ONG',
        'banner_subtitle': 'Nossa história até agora...',
        'banner_imagem': 'global/src/images/animalsobre.png',
    }
    return render(request, 'sobre.html',context=context)

def como_ajudar(request):
    context = {
        'banner_title': 'Como ajudar?',
        'banner_subtitle': 'Toda ajuda é bem-vinda! Procure formas de tranformar a vida de um pet.',
        'banner_imagem': 'global/src/images/banner-como-ajudar.png',
        'banner_button_text': 'Adotar',
    }
    
    return render(request, 'comoajudar.html',context=context)




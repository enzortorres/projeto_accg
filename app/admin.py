from django.utils.html import format_html
from django.contrib.admin import SimpleListFilter
from django.contrib import admin
from django import forms
from datetime import date
from app import models

class IdadeFilter(SimpleListFilter):
    title = 'idade'
    parameter_name = 'idade'

    def lookups(self, request, model_admin):
        return [
            ('0', 'Menos de 1 ano'),
            ('1-3', '1 a 3 anos'),
            ('4-6', '4 a 6 anos'),
            ('7+', '7 anos ou mais'),
        ]

    def queryset(self, request, queryset):
        hoje = date.today()

        if self.value() == '0':
            limite = hoje.replace(year=hoje.year - 1)
            return queryset.filter(data_nascimento__gt=limite)

        elif self.value() == '1-3':
            limite_inf = hoje.replace(year=hoje.year - 3)
            limite_sup = hoje.replace(year=hoje.year - 1)
            return queryset.filter(data_nascimento__lte=limite_sup, data_nascimento__gt=limite_inf)

        elif self.value() == '4-6':
            limite_inf = hoje.replace(year=hoje.year - 6)
            limite_sup = hoje.replace(year=hoje.year - 3)
            return queryset.filter(data_nascimento__lte=limite_sup, data_nascimento__gt=limite_inf)

        elif self.value() == '7+':
            limite = hoje.replace(year=hoje.year - 7)
            return queryset.filter(data_nascimento__lte=limite)

        return queryset

class AnimalAdminForm(forms.ModelForm):
    idade_anos = forms.IntegerField(label="Idade (anos)", min_value=0, required=False)
    idade_meses = forms.IntegerField(label="Meses", min_value=0, max_value=11, required=False)

    class Meta:
        model = models.Animal
        fields = ['nome', 'tipo', 'descricao']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if self.instance and self.instance.pk and self.instance.data_nascimento:
            hoje = date.today()
            anos = hoje.year - self.instance.data_nascimento.year
            meses = hoje.month - self.instance.data_nascimento.month
            if hoje.day < self.instance.data_nascimento.day:
                meses -= 1
            if meses < 0:
                anos -= 1
                meses += 12

            self.fields['idade_anos'].initial = anos
            self.fields['idade_meses'].initial = meses

    def save(self, commit=True):
        instance = super().save(commit=False)
        anos     = self.cleaned_data.get('idade_anos') or 0
        meses    = self.cleaned_data.get('idade_meses') or 0

        hoje = date.today()
        ano_nascimento = hoje.year - anos
        mes_nascimento = hoje.month - meses
        if mes_nascimento <= 0:
            ano_nascimento -= 1
            mes_nascimento += 12
        dia = min(hoje.day, 28)

        instance.data_nascimento = date(ano_nascimento, mes_nascimento, dia)

        if commit:
            instance.save()
        return instance

class AnimalFotoInline(admin.TabularInline):
    model = models.AnimalFoto
    extra = 1

class ResultadoTesteInline(admin.TabularInline):
    model = models.ResultadoTeste
    extra = 1  # número de formulários extras exibidos
@admin.register(models.Animal)
class AnimalAdmin(admin.ModelAdmin):
    form               = AnimalAdminForm
    list_display       = ('id', 'nome', 'sexo', 'porte', 'tipo','foto_admin', 'idade')
    list_display_links = ('id', 'nome',)
    list_filter        = ('tipo', 'sexo', 'porte',IdadeFilter,)
    inlines            = [AnimalFotoInline, ResultadoTesteInline]
    fields             = ('nome', 'sexo', 'tipo', 'porte', 'descricao', 'idade_anos', 'idade_meses')
    ordering           = ('id',)

    def idade(self, obj):
        if obj.data_nascimento:
            hoje  = date.today()
            anos  = hoje.year - obj.data_nascimento.year
            meses = hoje.month - obj.data_nascimento.month
            if hoje.day < obj.data_nascimento.day:
                meses -= 1
            if meses < 0:
                anos -= 1
                meses += 12
            return f"{anos} ano{'s' if anos != 1 else ''}" + (f" e {meses} mês{'es' if meses != 1 else ''}" if meses else "")
        return "-"
    
    def foto_admin(self, obj):
        primeira_foto = obj.fotos.first()
        if primeira_foto and primeira_foto.imagem:
            return format_html(f'<img src="{primeira_foto.imagem.url}" style="height: 50px;"/>')
        return "-"
    foto_admin.short_description = 'Foto'
    foto_admin.admin_order_field = 'fotos__imagem'  # permite ordenar por imagem

@admin.register(models.AnimalFoto)
class AnimalFotoAdmin(admin.ModelAdmin):
    list_display = ('animal', 'imagem')
    ordering     = ('id',)

@admin.register(models.ResultadoTeste)
class ResultadoTestesAdmin(admin.ModelAdmin):
    list_display = ('animal', 'nome_teste', 'resultado', 'data')
    ordering     = ('animal',)

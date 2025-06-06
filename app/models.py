from django.db import models
from datetime import date

def caminho_foto(instance, filename):
    tipo = instance.animal.tipo
    return f'fotos_animais/{tipo}/{filename}'

class Animal(models.Model):
    class Meta:
        verbose_name        = 'Animal'
        verbose_name_plural = 'Animais'
        db_table            = '"animal"'
    
    SEXO_CHOICES = [
        ('macho', 'Macho'),
        ('femea', 'Fêmea'),
    ]
    
    TIPO_CHOICES = [
        ('cachorro', 'Cachorro'),
        ('gato', 'Gato'),
    ]
    
    PORTE_CHOICES = [
        ('pequeno', 'Pequeno'),
        ('medio', 'Médio'),
        ('grande', 'Grande'),
    ]
    
    nome            = models.CharField(max_length=100)
    sexo            = models.CharField(max_length=20, choices=SEXO_CHOICES)
    porte           = models.CharField(max_length=20, choices=PORTE_CHOICES)
    tipo            = models.CharField(max_length=20, choices=TIPO_CHOICES)
    data_nascimento = models.DateField()
    descricao       = models.TextField(blank=True)
    disponivel      = models.BooleanField(default=True)
    
    @property
    def idade(self):
        hoje  = date.today()
        anos  = hoje.year - self.data_nascimento.year
        meses = hoje.month - self.data_nascimento.month
        
        if hoje.day < self.data_nascimento.day:
            meses -= 1
        if meses < 0:
            anos -= 1
            meses += 12

        partes = []
        if anos > 0:
            partes.append(f"{anos} ano" if anos == 1 else f"{anos} anos")
        if meses > 0:
            partes.append(f"{meses} mês" if meses == 1 else f"{meses} meses")

        return " e ".join(partes) if partes else "0 meses"
    
    def __str__(self):
        return self.nome

class AnimalFoto(models.Model):
    class Meta:
        verbose_name        = 'AnimalFoto'
        verbose_name_plural = 'AnimaisFotos'
        db_table            = '"animal_foto"'
    
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE, related_name='fotos')
    imagem = models.ImageField(upload_to=caminho_foto)
    
    def __str__(self):
        return f"Foto {self.animal.nome}"
    
class ResultadoTeste(models.Model):
    class Meta:
        verbose_name        = 'ResultadoTeste'
        verbose_name_plural = 'ResultadoTestes'
        db_table            = '"resultado_teste"'
    
    animal     = models.ForeignKey(Animal, on_delete=models.CASCADE, related_name='testes')
    nome_teste = models.CharField(max_length=100)
    resultado  = models.CharField(max_length=200)
    data       = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.nome_teste} - {self.animal.nome}"

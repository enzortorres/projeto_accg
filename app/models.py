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
    
    TIPO_CHOICES = [
        ('cachorro', 'Cachorro'),
        ('gato', 'Gato'),
    ]
    
    nome            = models.CharField(max_length=100)
    data_nascimento = models.DateField()
    descricao       = models.TextField(blank=True)  # deixei opcional para facilitar
    tipo            = models.CharField(max_length=20, choices=TIPO_CHOICES)
    
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

        if meses == 0:
            return f"{anos} anos"
        elif anos == 0:
            return f"{meses} meses"
        else:
            return f"{anos} anos e {meses} meses"
    
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

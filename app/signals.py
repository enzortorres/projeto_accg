import os
from django.db.models.signals import post_delete, pre_save
from django.dispatch import receiver
from .models import AnimalFoto

@receiver(post_delete, sender=AnimalFoto)
def deletar_arquivo_imagem(sender, instance, **kwargs):
    if instance.imagem:
        caminho = instance.imagem.path
        if os.path.isfile(caminho):
            os.remove(caminho)

@receiver(pre_save, sender=AnimalFoto)
def substituir_arquivo_imagem(sender, instance, **kwargs):
    if not instance.pk:
        return False

    try:
        imagem_antiga = AnimalFoto.objects.get(pk=instance.pk).imagem
    except AnimalFoto.DoesNotExist:
        return False

    nova_imagem = instance.imagem
    if not imagem_antiga == nova_imagem:
        if os.path.isfile(imagem_antiga.path):
            os.remove(imagem_antiga.path)

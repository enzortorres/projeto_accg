from django.core.management.base import BaseCommand
from app.models import Animal, AnimalFoto, ResultadoTeste

class Command(BaseCommand):
    help = "Apaga todos os animais, fotos e resultados de teste do banco de dados"

    def handle(self, *args, **options):
        fotos = AnimalFoto.objects.count()
        testes = ResultadoTeste.objects.count()
        animais = Animal.objects.count()

        self.stdout.write(f"Removendo {fotos} fotos, {testes} testes e {animais} animais...")

        AnimalFoto.objects.all().delete()
        ResultadoTeste.objects.all().delete()
        Animal.objects.all().delete()

        self.stdout.write(self.style.SUCCESS("Todos os dados foram apagados com sucesso."))
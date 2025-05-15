from django.core.management.base import BaseCommand
import random
import requests
from django.core.files.base import ContentFile
from datetime import date, timedelta
from faker import Faker
from app.models import Animal, AnimalFoto, ResultadoTeste

class Command(BaseCommand):
    help = "Gera animais aleatórios com fotos e testes"

    def add_arguments(self, parser):
        parser.add_argument('qtd', type=int, help="Quantidade de animais")

    def handle(self, *args, **options):
        fake = Faker()
        TIPOS = ['cachorro', 'gato']
        TESTES = ['Parvovírus', 'Raiva', 'Leishmaniose', 'Coronavírus Canino', 'FIV', 'Felv']
        SEXOS = ['macho', 'femea']
        PORTES = ['pequeno', 'medio', 'grande']
        qtd = options['qtd']

        for _ in range(qtd):
            nome            = fake.first_name()
            tipo            = random.choice(TIPOS)
            sexo            = random.choice(SEXOS)
            porte           = random.choice(PORTES)
            descricao       = fake.text(max_nb_chars=200)
            dias_atras      = random.randint(30, 365 * 10)
            data_nascimento = date.today() - timedelta(days=dias_atras)
            self.stdout.write(self.style.WARNING(f"Criando {tipo}: {nome}"))

            animal = Animal.objects.create(
                nome=nome,
                sexo=sexo,
                tipo=tipo,
                porte=porte,
                descricao=descricao,
                data_nascimento=data_nascimento,
            )

            # > Fotos
            for i in range(random.randint(1, 3)):
                tentativas = 0
                while tentativas < 5:
                    try:
                        if tipo == 'cachorro':
                            resp = requests.get('https://dog.ceo/api/breeds/image/random')
                            resp.raise_for_status()
                            url_imagem = resp.json()['message']
                        else:
                            resp = requests.get('https://api.thecatapi.com/v1/images/search')
                            resp.raise_for_status()
                            url_imagem = resp.json()[0]['url']

                        ext = url_imagem.split('.')[-1].lower()
                        if ext not in ['jpg', 'jpeg', 'png']:
                            tentativas += 1
                            continue  # tenta outra imagem

                        img_resp = requests.get(url_imagem)
                        img_resp.raise_for_status()

                        nome_arquivo = f"{tipo}_{nome}_{i}.{ext}"
                        imagem = ContentFile(img_resp.content, name=nome_arquivo)
                        AnimalFoto.objects.create(animal=animal, imagem=imagem)
                        break  # imagem válida salva, sai do while
                    except Exception as e:
                        self.stderr.write(f"Erro ao baixar imagem: {e}")
                        tentativas += 1
                else:
                    self.stderr.write(f"Não foi possível obter uma imagem válida para {tipo} {nome}")
                    
            # > Testes
            for _ in range(random.randint(1, 3)):
                nome_teste = random.choice(TESTES)
                resultado = random.choice([
                    "Negativo", "Positivo leve", "Positivo moderado", "Positivo severo"
                ])
                data_teste = date.today() - timedelta(days=random.randint(0, 30))
                ResultadoTeste.objects.create(
                    animal=animal,
                    nome_teste=nome_teste,
                    resultado=resultado,
                    data=data_teste
                )
            self.stdout.write(self.style.SUCCESS(f"Animal {nome} criado com sucesso!\n"))

        self.stdout.write(self.style.SUCCESS(f"{qtd} animais criados com sucesso!"))

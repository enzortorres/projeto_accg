# Generated by Django 5.2 on 2025-06-13 18:33

import app.models
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('sexo', models.CharField(choices=[('macho', 'Macho'), ('femea', 'Fêmea')], max_length=20)),
                ('porte', models.CharField(choices=[('pequeno', 'Pequeno'), ('medio', 'Médio'), ('grande', 'Grande')], max_length=20)),
                ('tipo', models.CharField(choices=[('cachorro', 'Cachorro'), ('gato', 'Gato')], max_length=20)),
                ('data_nascimento', models.DateField()),
                ('descricao', models.TextField(blank=True)),
                ('disponivel', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Animal',
                'verbose_name_plural': 'Animais',
                'db_table': '"animal"',
            },
        ),
        migrations.CreateModel(
            name='AnimalFoto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagem', models.ImageField(upload_to=app.models.caminho_foto)),
                ('animal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fotos', to='app.animal')),
            ],
            options={
                'verbose_name': 'AnimalFoto',
                'verbose_name_plural': 'AnimaisFotos',
                'db_table': '"animal_foto"',
            },
        ),
        migrations.CreateModel(
            name='ResultadoTeste',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_teste', models.CharField(max_length=100)),
                ('resultado', models.CharField(max_length=200)),
                ('data', models.DateField(auto_now_add=True)),
                ('animal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='testes', to='app.animal')),
            ],
            options={
                'verbose_name': 'ResultadoTeste',
                'verbose_name_plural': 'ResultadoTestes',
                'db_table': '"resultado_teste"',
            },
        ),
    ]

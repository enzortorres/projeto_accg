# Generated by Django 5.2 on 2025-05-15 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_alter_animal_sexo'),
    ]

    operations = [
        migrations.AddField(
            model_name='animal',
            name='porte',
            field=models.CharField(choices=[('pequeno', 'Pequeno'), ('medio', 'Médio'), ('grande', 'Grande')], default='grande', max_length=20),
        ),
        migrations.AlterField(
            model_name='animal',
            name='sexo',
            field=models.CharField(choices=[('masculino', 'Masculino'), ('feminino', 'Feminino')], max_length=20),
        ),
    ]

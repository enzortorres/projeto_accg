# Generated by Django 5.2 on 2025-05-15 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_alter_animal_porte'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal',
            name='sexo',
            field=models.CharField(choices=[('macho', 'Macho'), ('femea', 'Fêmea')], max_length=20),
        ),
    ]

# Generated by Django 5.0.4 on 2024-04-10 22:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alunos', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='campus',
            options={'verbose_name_plural': 'Campus'},
        ),
        migrations.AlterModelOptions(
            name='vinculacao',
            options={'verbose_name_plural': 'Vinculação'},
        ),
    ]

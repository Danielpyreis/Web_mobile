# Generated by Django 5.0.2 on 2024-04-15 02:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alunos', '0004_merge_20240414_2317'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vinculacao',
            name='situacao',
            field=models.CharField(choices=[('Vinculado', 'Vinculado'), ('Formado', 'Formado'), ('Evadido', 'Evadido'), ('Jubilado', 'Jubilado')], default='Vinculado', max_length=20),
        ),
    ]

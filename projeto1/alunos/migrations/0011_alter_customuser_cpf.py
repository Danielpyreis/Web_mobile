# Generated by Django 4.2.11 on 2024-06-10 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alunos', '0010_alter_customuser_groups_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='cpf',
            field=models.CharField(max_length=11, unique=True),
        ),
    ]
# Generated by Django 4.2.11 on 2024-06-10 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alunos', '0011_alter_customuser_cpf'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customuser',
            old_name='is_staff',
            new_name='is_admin',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='is_superuser',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='user_permissions',
        ),
        migrations.AlterField(
            model_name='customuser',
            name='cpf',
            field=models.CharField(max_length=14, unique=True, verbose_name='CPF'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='email',
            field=models.EmailField(max_length=255, unique=True, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='nome',
            field=models.CharField(max_length=255, verbose_name='Nome'),
        ),
    ]
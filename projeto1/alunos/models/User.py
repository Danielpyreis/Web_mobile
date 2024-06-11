from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class CustomUserManager(BaseUserManager):
    def create_user(self, email, cpf, nome, password=None):
        if not email:
            raise ValueError('O Email é obrigatório')
        if not cpf:
            raise ValueError('O CPF é obrigatório')
        if not nome:
            raise ValueError('O Nome é obrigatório')

        email = self.normalize_email(email)
        user = self.model(
            email=email,
            cpf=cpf,
            nome=nome,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, cpf, nome, password=None):
        user = self.create_user(
            email=email,
            cpf=cpf,
            nome=nome,
            password=password,
        )
        user.is_admin = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class CustomUser(AbstractBaseUser):
    email = models.EmailField(verbose_name='Email', max_length=255, unique=True)
    cpf = models.CharField(verbose_name='CPF', max_length=14, unique=True)
    nome = models.CharField(verbose_name='Nome', max_length=255)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['cpf', 'nome']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

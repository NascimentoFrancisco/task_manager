from django.db import models
from django.contrib.auth.models import (
        AbstractBaseUser, PermissionsMixin, UserManager
    )



class User(AbstractBaseUser, PermissionsMixin):

    
    username = models.CharField(
        'Usuário', max_length=30, null=False, blank=False,
        unique=True, error_messages={'unique' : "Usuário já cadastrado!"},
        help_text='Um nome curto para a sua identificação exclusiva no sistema.'
    )

    name = models.CharField(
        'Nome', max_length=255, null=False, blank=False
    )

    email = models.EmailField(
        'E-mail', blank=False, null=False, unique=True,
        error_messages = {'unique' : "E-mail já cadastrado!"},
        help_text = 'Para envio de notificações se caso necessário.'
    )

    is_staff = models.BooleanField(default = False)
    is_superuser = models.BooleanField(default = False)
    is_active = models.BooleanField(default = True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    objects = UserManager()

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'usuário'
        verbose_name_plural = 'usuários'
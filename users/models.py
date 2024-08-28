from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class User(AbstractUser):
    """Модель пользователя, где изменено имя пользователя на почту. Так же реализована верификация пользователя по почте"""
    username = None
    email = models.EmailField(unique=True, verbose_name='Почта пользователя')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.email

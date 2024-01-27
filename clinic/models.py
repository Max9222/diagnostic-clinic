from django.db import models
from django.conf import settings

NULLABLE = {'blank': True, 'null': True}

class Area(models.Model):

    name = models.CharField(max_length=100, verbose_name='название', unique=True)
    description = models.TextField(verbose_name='описание')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'направление'
        verbose_name_plural = 'направления'


class Team(models.Model):

    name = models.CharField(max_length=150, verbose_name='имя')
    phone = models.CharField(max_length=25, verbose_name='телефон')
    email = models.EmailField(verbose_name='почта', unique=True)

    area = models.ForeignKey(Area, on_delete=models.CASCADE, verbose_name='направление')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'команда'
        verbose_name_plural = 'команды'


class Clinic(models.Model):

    name = models.CharField(max_length=100, verbose_name='название', unique=True)
    description = models.TextField(verbose_name='описание')
    address = models.CharField(max_length=50, verbose_name='адрес')
    phone = models.CharField(max_length=25, verbose_name='номер')
    email = models.EmailField(verbose_name='почта', unique=True)

    area = models.ForeignKey(Area, on_delete=models.CASCADE, verbose_name='Направление')
    team = models.ForeignKey(Team, on_delete=models.CASCADE, verbose_name='Команда')

    def __str__(self):
        return f'{self.name} - {self.description}'

    class Meta:
        verbose_name = 'клиника'
        verbose_name_plural = 'клиники'


class Client(models.Model):

    email = models.EmailField(unique=True, verbose_name='Email')
    name = models.CharField(max_length=100, verbose_name='ФИО', **NULLABLE)
    phone = models.CharField(max_length=35, verbose_name='номер телефона', **NULLABLE)
    comment = models.TextField(verbose_name='Комментарий', **NULLABLE)
    avatar = models.ImageField(upload_to='clinic/', verbose_name='аватар', **NULLABLE)

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Клиент', **NULLABLE
    )

    def __str__(self):
        return f'{self.email}'

    class Meta:
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"

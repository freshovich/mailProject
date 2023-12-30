from django.contrib.auth.models import AbstractUser
from django.db import models
from django.dispatch import Signal

user_registrated = Signal()


class Dolzn(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')

    class Meta:
        verbose_name = 'Должность'
        verbose_name_plural = 'Должности'


class AdvUser(AbstractUser):
    dolzn = models.ForeignKey(Dolzn, on_delete=models.CASCADE, verbose_name='Должность', null=True, blank=True)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username

    def get_current_user(request):
        user = request.user
        return user

    def delete(self, *args, **kwargs):
        for bb in self.additionalimage_set.all():
            bb.delete()
        super().delete(*args, **kwargs)

    class Meta:
        pass


class Mail(models.Model):
    sender = models.ForeignKey(AdvUser, on_delete=models.CASCADE,
                               verbose_name='Отправитель',
                               related_name='sender')
    recipient = models.ForeignKey(AdvUser, on_delete=models.CASCADE, verbose_name='Получатель', related_name='recipient')
    theme = models.CharField("Тема письма", max_length=255)
    description = models.TextField('Текст')
    file = models.FileField(upload_to='files/')

    class Meta:
        verbose_name = 'Письмо'
        verbose_name_plural = 'Письма'

    def __str__(self):
        return f"{self.sender.username} - {self.recipient.username} {self.theme}"

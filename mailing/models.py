from django.core.mail import send_mail
from django.db import models

from config.settings import EMAIL_HOST
from users.models import CustomUser


class MailingGet(models.Model):
    """ Модель "Получатель рассылки" """
    email = models.EmailField(unique=True, verbose_name='Email')
    name = models.CharField(max_length=60, blank=True, null=True, verbose_name='Имя')
    comment = models.TextField(max_length=200, blank=True, null=True, verbose_name='Комментарий')
    owner = models.ForeignKey(CustomUser, verbose_name='Владелец', blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.email} {self.comment}'

    class Meta:
        verbose_name = 'получатель'
        verbose_name_plural = 'получатели'
        ordering = ['email']
        permissions = [
            ('can_moderate_mailing_get', 'Can moderate mailing get'),
        ]


class Message(models.Model):
    """ Модель "Сообщение" """
    mail_theme = models.CharField(max_length=100, verbose_name='Тема письма')
    mail_body = models.TextField(verbose_name='Тело письма')
    owner = models.ForeignKey(CustomUser, verbose_name='Владелец', blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.mail_theme}'

    class Meta:
        verbose_name = 'сообщение'
        verbose_name_plural = 'сообщения'
        ordering = ['mail_theme']
        permissions = [
            ('can_moderate_messages', 'Can moderate messages'),
        ]


class MailingList(models.Model):
    """ Модель "Рассылка" """
    time_first = models.DateTimeField(verbose_name='Дата и время первой отправки', help_text='YYYY-MM-DD HH:MM:SS')
    time_last = models.DateTimeField(verbose_name='Дата и время окончания отправки', help_text='YYYY-MM-DD HH:MM:SS')
    status = models.CharField(max_length=9, verbose_name='Статус рассылки', help_text='Создана, Запущена, Завершена')
    message = models.ForeignKey(Message, on_delete=models.CASCADE, verbose_name='Сообщение')
    recipient = models.ManyToManyField(MailingGet, verbose_name='Получатель рассылки')
    owner = models.ForeignKey(CustomUser, verbose_name='Владелец', blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.message} {self.status}'

    def send_mailing_list(self):
        recipients = self.recipient.all()
        for recipient in recipients:
            send_mail(
                subject=self.message.mail_theme,
                message=self.message.mail_body,
                from_email=EMAIL_HOST.USER,
                recipient_list=[recipient.email]
            )
        return len(recipients)

    class Meta:
        verbose_name = 'рассылка'
        verbose_name_plural = 'рассылки'
        ordering = ['status']
        permissions = [
            ('can_moderate_mailing_list', 'Can moderate mailing list'),
        ]


class AttemptMailing(models.Model):
    """ Модель "Попытка рассылки" """
    attempt_time = models.DateTimeField(verbose_name='Дата и время попытки')
    status = models.CharField(max_length=10, verbose_name='Статус', help_text='Успешно, Не успешно')
    server_answer = models.TextField(verbose_name='Ответ почтового сервера')
    mailing_list = models.ForeignKey(MailingList, on_delete=models.CASCADE, verbose_name='Рассылка')

from django.db import models

class MailingGet(models.Model):
    email = models.EmailField(unique=True, verbose_name='Email')
    name = models.CharField(max_length=60, blank=True, null=True, verbose_name='Имя')
    comment = models.TextField(max_length=200, blank=True, null=True, verbose_name='Комментарий')

    def __str__(self):
        return f'{self.email} {self.comment}'

    class Meta:
        verbose_name = 'получатель'
        verbose_name_plural = 'получатели'
        ordering = ['email']

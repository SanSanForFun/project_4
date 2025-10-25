from celery import shared_task
from django.core.mail import send_mail
from mailing.models import MailingList, Message

@shared_task
def send_mailing(mailing_id):
    mailing = MailingList.objects.get(id=mailing_id)
    recipients = mailing.recipients.all()  # Получаем всех получателей рассылки
    message = mailing.message  # Получаем сообщение для рассылки

    for recipient in recipients:
        send_mail(
            subject=message.subject,
            message=message.body,
            from_email='your_email@example.com',
            recipient_list=[recipient.email],
            fail_silently=False,
        )
from django.core.management.base import BaseCommand
from django.utils import timezone
from mailing.models import MailingList
from mailing.tasks import send_mailing  # Предполагается, что отправка выполняется через Celery


class Command(BaseCommand):
    help = 'Отправляет рассылку по ID'

    def add_arguments(self, parser):
        parser.add_argument('mailing_id', type=int, help='ID рассылки')

    def handle(self, *args, **kwargs):
        mailing_id = kwargs['mailing_id']
        try:
            mailing = MailingList.objects.get(id=mailing_id)

            # Запускаем задачу отправки рассылки (например, через Celery)
            send_mailing.delay(mailing.id)

            self.stdout.write(self.style.SUCCESS(f"Рассылка {mailing_id} успешно запущена!"))
        except MailingList.DoesNotExist:
            self.stderr.write(self.style.ERROR(f"Рассылка с ID {mailing_id} не найдена."))
from django.core.cache import cache

from config.settings import CACHE_ENABLED
from mailing.models import MailingList, MailingGet


def get_news_letters_from_cache():
    """ Получаем данные по рассылкам из кэша. Если нет, то из БД """
    if not CACHE_ENABLED:
        return MailingList.objects.all()
    key = 'mailing_list'
    mailing_list = cache.get(key)
    if mailing_list is not None:
        return mailing_list
    mailing_list = MailingList.objects.all()
    cache.set(key, mailing_list)
    return mailing_list


class HomeService:

    @staticmethod
    def count_mailing_list(user):
        mailing_list = MailingList.objects.filter(owner=user)
        # Если рассылок нет возвращаем None
        if not mailing_list.exists():
            return 0
        return mailing_list.count()

    @staticmethod
    def count_active_mailing_list(user):
        mailing_list = MailingList.objects.filter(status='Запущена', owner=user)
        # Если рассылок нет возвращаем None
        if not mailing_list.exists():
            return 0
        return mailing_list.count()

    @staticmethod
    def count_unique_mailing_get(user):
        mailing_list = MailingGet.objects.filter(owner=user)
        # Если рассылок нет возвращаем None
        if not mailing_list.exists():
            return 0
        return mailing_list.count()

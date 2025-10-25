from django.contrib import admin
from mailing.models import MailingGet, Message, MailingList, AttemptMailing


@admin.register(MailingGet)
class MailingGetAdmin(admin.ModelAdmin):
    list_display = ('id', 'email',)
    list_filter = ('email',)
    search_fields = ('email',)


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('mail_theme',)
    search_fields = ('mail_theme',)


@admin.register(MailingList)
class MailingListAdmin(admin.ModelAdmin):
    list_display = ('time_first', 'time_last', 'status', 'message')
    list_filter = ('time_first', 'time_last', 'status')
    search_fields = ('status', 'message')

@admin.register(AttemptMailing)
class AttemptMailingAdmin(admin.ModelAdmin):
    list_display = ('attempt_time', 'status', 'mailing_list')
    list_filter = ('attempt_time', 'status')
    search_fields = ('status', 'mailing_list')
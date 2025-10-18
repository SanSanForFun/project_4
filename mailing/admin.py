from django.contrib import admin
from mailing.models import MailingGet


@admin.register(MailingGet)
class MailingGetAdmin(admin.ModelAdmin):
    list_display = ('id', 'email',)
    list_filter = ('email',)
    search_fields = ('email',)

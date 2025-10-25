from django.forms import ModelForm, BooleanField
from mailing.models import MailingGet, Message, MailingList, AttemptMailing


class MessageForm(ModelForm):
    """ Сообщения """

    class Meta:
        model = Message
        fields = ['mail_theme', 'mail_body', ]


class MailingGetForm(ModelForm):
    """ Получатель рассылки """

    class Meta:
        model = MailingGet
        fields = ['email', 'name', 'comment']


class MailingListForm(ModelForm):
    """ Рассылка """

    class Meta:
        model = MailingList
        exclude = ['owner']

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request')
        user = self.request.user
        super().__init__(*args, **kwargs)
        self.fields['email'].queryset = MailingGet.objects.filter(owner=user)
        self.fields['message'].queryset = Message.objects.filter(owner=user)


class AttemptMailingForm(ModelForm):
    """ Попытка рассылки """

    class Meta:
        model = AttemptMailing
        fields = ['attempt_time', 'status', 'server_answer', 'mailing_list']


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, fild in self.fields.items():
            if isinstance(fild, BooleanField):
                fild.widget.attrs['class'] = 'form-check-input'
            else:
                fild.widget.attrs['class'] = 'form-control'

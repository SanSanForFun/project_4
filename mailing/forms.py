from django.forms import ModelForm, BooleanField
from mailing.models import MailingGet, Message


class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = ['mail_theme', 'mail_body',]

class MailingGetForm(ModelForm):
    class Meta:
        model = MailingGet
        fields = ['email', 'name', 'comment']


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, fild in self.fields.items():
            if isinstance(fild, BooleanField):
                fild.widget.attrs['class'] = 'form-check-input'
            else:
                fild.widget.attrs['class'] = 'form-control'
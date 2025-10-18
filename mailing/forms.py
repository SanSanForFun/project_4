from django.forms import ModelForm
from mailing.models import MailingGet


class ProductForm(ModelForm):
    class Meta:
        model = MailingGet
        fields = ['email', 'name', 'comment', ]

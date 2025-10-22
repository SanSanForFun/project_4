from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from mailing.forms import MessageForm, MailingGetForm
from mailing.models import MailingGet, Message


## Класс получатель рассылок
# Просмотр списка клиентов
class MailingGetListView(ListView):
    model = MailingGet
    template_name = 'mailing/mailing_get_list.html'


# Информация о клиенте
class MailingGetDetailView(DetailView):
    model = MailingGet
    template_name = 'mailing/mailing_get_detail.html'



# Создание клиента
class MailingGetCreateView(CreateView):
    model = MailingGet
    form_class = MailingGetForm
    template_name = 'mailing/mailing_get_create.html'
    success_url = reverse_lazy('mailing:mailing_get_list')


# Редактирование клиента
class MailingGetUpdateView(UpdateView):
    model = MailingGet
    form_class = MailingGetForm
    template_name = 'mailing/mailing_get_update.html'
    success_url = reverse_lazy('mailing:mailing_get_list')


# Удаление клиента
class MailingGetDeleteView(DeleteView):
    model = MailingGet
    # permission_required = 'catalog.can_unpublish_products'
    template_name = 'mailing/mailing_get_delete.html'
    success_url = reverse_lazy('mailing:mailing_get_list')

# Класс Сообщение
# Просмотр списка сообщений
class MessageListView(ListView):
    model = Message
    template_name = 'message_list.html'


# Информация о сообщении
class MessageDetailView(DetailView):
    model = Message


# Создание сообщения
class MessageCreateView(CreateView):
    model = Message
    form_class = MessageForm
    template_name = 'mailing/message_create.html'
    success_url = reverse_lazy('mailing:message_list')


# Редактирование сообщения
class MessageUpdateView(UpdateView):
    model = Message
    form_class = MessageForm
    template_name = 'mailing/message_update.html'
    success_url = reverse_lazy('mailing:message_list')


# Удаление сообщения
class MessageDeleteView(DeleteView):
    model = Message
    #permission_required = 'catalog.can_unpublish_products'
    template_name = 'mailing/message_delete.html'
    success_url = reverse_lazy('mailing:message_list')

# Класс Рассылка
# Просмотр списка рассылок
class MailingListView(ListView):
    model = MailingGet
    template_name = 'mailing/mailing_list.html'


# Информация о рассылке
class MailingDetailView(DetailView):
    model = MailingGet


# Создание рассылки
class MailingCreateView(CreateView):
    model = MailingGet
    # form_class = ProductForm
    # template_name = 'catalog/products_form.html'
    success_url = reverse_lazy('mailing:mailing_list')


# Редактирование рассылки
class MailingUpdateView(UpdateView):
    model = MailingGet
    # form_class = ProductForm
    # template_name = 'catalog/products_form.html'
    success_url = reverse_lazy('mailing:mailing_list')


# Удаление рассылки
class MailingDeleteView(DeleteView):
    model = MailingGet
    # permission_required = 'catalog.can_unpublish_products'
    # template_name = 'catalog/products_confirm_delete.html'
    success_url = reverse_lazy('mailing:mailing_list')
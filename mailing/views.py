from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from mailing.forms import MessageForm, MailingGetForm, MailingListForm
from mailing.models import MailingGet, Message, MailingList


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
class MailingGetCreateView(LoginRequiredMixin, CreateView):
    model = MailingGet
    form_class = MailingGetForm
    template_name = 'mailing/mailing_get_create.html'
    success_url = reverse_lazy('mailing:mailing_get_list')


# Редактирование клиента
class MailingGetUpdateView(LoginRequiredMixin, UpdateView):
    model = MailingGet
    form_class = MailingGetForm
    template_name = 'mailing/mailing_get_update.html'
    success_url = reverse_lazy('mailing:mailing_get_list')


# Удаление клиента
class MailingGetDeleteView(LoginRequiredMixin, DeleteView):
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
class MessageCreateView(LoginRequiredMixin, CreateView):
    model = Message
    form_class = MessageForm
    template_name = 'mailing/message_create.html'
    success_url = reverse_lazy('mailing:message_list')


# Редактирование сообщения
class MessageUpdateView(LoginRequiredMixin, UpdateView):
    model = Message
    form_class = MessageForm
    template_name = 'mailing/message_update.html'
    success_url = reverse_lazy('mailing:message_list')


# Удаление сообщения
class MessageDeleteView(LoginRequiredMixin, DeleteView):
    model = Message
    #permission_required = 'catalog.can_unpublish_products'
    template_name = 'mailing/message_delete.html'
    success_url = reverse_lazy('mailing:message_list')

# Класс Рассылка
# Просмотр списка рассылок
class MailingListView(ListView):
    model = MailingList
    template_name = 'mailing/mailing_list.html'


# Информация о рассылке
class MailingListDetailView(DetailView):
    model = MailingList
    template_name = 'mailing/mailing_list_detail.html'


# Создание рассылки
class MailingListCreateView(LoginRequiredMixin, CreateView):
    model = MailingList
    form_class = MailingListForm
    template_name = 'mailing/mailing_list_create.html'
    success_url = reverse_lazy('mailing:mailing_list')


# Редактирование рассылки
class MailingListUpdateView(LoginRequiredMixin, UpdateView):
    model = MailingList
    form_class = MailingListForm
    template_name = 'mailing/mailing_list_update.html'
    success_url = reverse_lazy('mailing:mailing_list')


# Удаление рассылки
class MailingListDeleteView(LoginRequiredMixin, DeleteView):
    model = MailingList
    # permission_required = 'catalog.can_unpublish_products'
    template_name = 'mailing/mailing_list_delete.html'
    success_url = reverse_lazy('mailing:mailing_list')
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from mailing.models import MailingGet


## Класс получатель рассылок
# Просмотр списка клиентов
class MailingGetListView(ListView):
    model = MailingGet
    template_name = 'mailing/mailing_list.html'


# Информация о клиенте
class MailingGetDetailView(DetailView):
    model = MailingGet


# Создание клиента
class MailingGetCreateView(CreateView):
    model = MailingGet
    # form_class = ProductForm
    # template_name = 'catalog/products_form.html'
    # success_url = reverse_lazy('catalog:products_list')


# Редактирование клиента
class MailingGetUpdateView(UpdateView):
    model = MailingGet
    # form_class = ProductForm
    # template_name = 'catalog/products_form.html'
    # success_url = reverse_lazy('catalog:products_list')


# Удаление клиента
class MailingGetDeleteView(DeleteView):
    model = MailingGet
    # permission_required = 'catalog.can_unpublish_products'
    # template_name = 'catalog/products_confirm_delete.html'
    # success_url = reverse_lazy('catalog:products_list')

# Класс Сообщение
# Просмотр списка сообщений
class MessageListView(ListView):
    model = MailingGet
    template_name = 'mailing/message_list.html'


# Информация о сообщении
class MessageDetailView(DetailView):
    model = MailingGet


# Создание сообщения
class MessageCreateView(CreateView):
    model = MailingGet
    # form_class = ProductForm
    # template_name = 'catalog/products_form.html'
    # success_url = reverse_lazy('catalog:products_list')


# Редактирование сообщения
class MessageUpdateView(UpdateView):
    model = MailingGet
    # form_class = ProductForm
    # template_name = 'catalog/products_form.html'
    # success_url = reverse_lazy('catalog:products_list')


# Удаление сообщения
class MessageDeleteView(DeleteView):
    model = MailingGet
    # permission_required = 'catalog.can_unpublish_products'
    # template_name = 'catalog/products_confirm_delete.html'
    # success_url = reverse_lazy('catalog:products_list')

# Класс Рассылка
# Просмотр списка рассылок
class MailingListListView(ListView):
    model = MailingGet
    template_name = 'mailing/mailing_list.html'


# Информация о рассылке
class MailingListDetailView(DetailView):
    model = MailingGet


# Создание рассылки
class MailingListCreateView(CreateView):
    model = MailingGet
    # form_class = ProductForm
    # template_name = 'catalog/products_form.html'
    success_url = reverse_lazy('mailing:mailing_list')


# Редактирование рассылки
class MailingListUpdateView(UpdateView):
    model = MailingGet
    # form_class = ProductForm
    # template_name = 'catalog/products_form.html'
    success_url = reverse_lazy('mailing:mailing_list')


# Удаление рассылки
class MailingListDeleteView(DeleteView):
    model = MailingGet
    # permission_required = 'catalog.can_unpublish_products'
    # template_name = 'catalog/products_confirm_delete.html'
    success_url = reverse_lazy('mailing:mailing_list')
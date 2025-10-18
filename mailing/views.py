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
    #form_class = ProductForm
    #template_name = 'catalog/products_form.html'
    #success_url = reverse_lazy('catalog:products_list')


# Редактирование клиента
class MailingGetUpdateView(UpdateView):
    model = MailingGet
    #form_class = ProductForm
    #template_name = 'catalog/products_form.html'
    #success_url = reverse_lazy('catalog:products_list')


# Удаление клиента
class MailingGetDeleteView(DeleteView):
    model = MailingGet
    # permission_required = 'catalog.can_unpublish_products'
    # template_name = 'catalog/products_confirm_delete.html'
    # success_url = reverse_lazy('catalog:products_list')

# Класс Сообщение

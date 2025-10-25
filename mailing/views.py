from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView

from mailing.forms import MessageForm, MailingGetForm, MailingListForm
from mailing.models import MailingGet, Message, MailingList, AttemptMailing
from mailing.services import HomeService
from django.contrib import messages
from mailing.tasks import send_mailing


class HomeTemplateView(TemplateView):
    template_name = 'base.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        if user.is_authenticated:
            context['count_mailing_list'] = HomeService.count_mailing_list(user)
            context['count_active_mailing_list'] = HomeService.count_active_mailing_list(user)
            context['count_unique_mailing_get'] = HomeService.count_unique_mailing_get(user)


## Класс получатель рассылок
# Просмотр списка клиентов
@method_decorator(cache_page(60 * 15), name='dispatch')
class MailingGetListView(ListView):
    model = MailingGet
    template_name = 'mailing/mailing_get_list.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        if (self.request.user.has_perm('service.can_moderate_mailing_list') or self.request.user.is_superuser):
            return queryset
        return queryset.filter(owner=self.request.user)


# Информация о клиенте
@method_decorator(cache_page(60 * 15), name='dispatch')
class MailingGetDetailView(DetailView):
    model = MailingGet
    template_name = 'mailing/mailing_get_detail.html'


# Создание клиента
class MailingGetCreateView(LoginRequiredMixin, CreateView):
    model = MailingGet
    form_class = MailingGetForm
    template_name = 'mailing/mailing_get_create.html'
    success_url = reverse_lazy('mailing:mailing_get_list')

    def form_valid(self, form):
        mailing_get = form.save()
        user = self.request.user
        mailing_get.owner = user
        mailing_get.save()
        return super().form_valid(form)


# Редактирование клиента
class MailingGetUpdateView(LoginRequiredMixin, UpdateView):
    model = MailingGet
    form_class = MailingGetForm
    template_name = 'mailing/mailing_get_update.html'
    success_url = reverse_lazy('mailing:mailing_get_list')

    def get_form_class(self):
        user = self.request.user
        if user == self.object.owner:
            return MailingGetForm
        raise PermissionDenied


# Удаление клиента
class MailingGetDeleteView(LoginRequiredMixin, DeleteView):
    model = MailingGet
    template_name = 'mailing/mailing_get_delete.html'
    success_url = reverse_lazy('mailing:mailing_get_list')


# Класс Сообщение
# Просмотр списка сообщений
@method_decorator(cache_page(60 * 15), name='dispatch')
class MessageListView(ListView):
    model = Message
    template_name = 'message_list.html'


# Информация о сообщении
@method_decorator(cache_page(60 * 15), name='dispatch')
class MessageDetailView(DetailView):
    model = Message


# Создание сообщения
class MessageCreateView(LoginRequiredMixin, CreateView):
    model = Message
    form_class = MessageForm
    template_name = 'mailing/message_create.html'
    success_url = reverse_lazy('mailing:message_list')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


# Редактирование сообщения
class MessageUpdateView(LoginRequiredMixin, UpdateView):
    model = Message
    form_class = MessageForm
    template_name = 'mailing/message_update.html'
    success_url = reverse_lazy('mailing:message_list')


# Удаление сообщения
class MessageDeleteView(LoginRequiredMixin, DeleteView):
    model = Message
    template_name = 'mailing/message_delete.html'
    success_url = reverse_lazy('mailing:message_list')


# Класс Рассылка
# Просмотр списка рассылок
@method_decorator(cache_page(60 * 15), name='dispatch')
class MailingListView(ListView):
    model = MailingList
    template_name = 'mailing/mailing_list.html'


# Информация о рассылке
@method_decorator(cache_page(60 * 15), name='dispatch')
class MailingListDetailView(DetailView):
    model = MailingList
    template_name = 'mailing/mailing_list_detail.html'


# Создание рассылки
class MailingListCreateView(LoginRequiredMixin, CreateView):
    model = MailingList
    form_class = MailingListForm
    template_name = 'mailing/mailing_list_create.html'
    success_url = reverse_lazy('mailing:mailing_list')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


# Редактирование рассылки
class MailingListUpdateView(LoginRequiredMixin, UpdateView):
    model = MailingList
    form_class = MailingListForm
    template_name = 'mailing/mailing_list_update.html'
    success_url = reverse_lazy('mailing:mailing_list')


# Удаление рассылки
class MailingListDeleteView(LoginRequiredMixin, DeleteView):
    model = MailingList
    template_name = 'mailing/mailing_list_delete.html'
    success_url = reverse_lazy('mailing:mailing_list')


class AttemptMailingListView(LoginRequiredMixin, ListView):
    model = AttemptMailing
    template_name = 'mailing/attempt_mailing_list.html'


class SendMailingView(ListView):
    model = MailingList
    template_name = 'mailing/send_mailing.html'

    def send_mailing_view(request):
        if request.method == 'POST':
            form = MailingListForm(request.POST, user=request.user)
            if form.is_valid():
                mailing = form.cleaned_data['mailing']

                # Запускаем задачу отправки рассылки (например, через Celery)
                send_mailing.delay(mailing.id)

                messages.success(request, "Рассылка успешно запущена!")
                return redirect('mailing_list')  # Перенаправляем на список рассылок
        else:
            form = MailingListForm(user=request.user)

        return render(request, 'send_mailing.html', {'form': form})

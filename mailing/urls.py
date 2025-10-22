from tempfile import template

from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.views.decorators.cache import cache_page

from .models import MailingGet
from .views import MailingGetListView, MailingListView, MessageListView, MessageDetailView, MessageCreateView, \
    MessageDeleteView, MessageUpdateView, MailingGetDetailView, MailingGetUpdateView, \
    MailingGetCreateView, MailingGetDeleteView, MailingListDetailView, MailingListUpdateView, MailingListCreateView, \
    MailingListDeleteView

app_name = 'mailing'

urlpatterns = [
    path('mailing_list', MailingListView.as_view(), name='mailing_list'),
    path('mailing_list/<int:pk>/', MailingListDetailView.as_view(), name='mailing_list_detail'),
    path('mailing_list/update/<int:pk>/', MailingListUpdateView.as_view(), name='mailing_list_update'),
    path('mailing_list/create/', MailingListCreateView.as_view(), name='mailing_list_create'),
    path('mailing_list/delete/<int:pk>/', MailingListDeleteView.as_view(), name='mailing_list_delete'),
    path('message/', MessageListView.as_view(), name='message_list'),
    path('message/<int:pk>/', MessageDetailView.as_view(), name='message_detail'),
    path('message/update/<int:pk>/', MessageUpdateView.as_view(), name='message_update'),
    path('message/create/', MessageCreateView.as_view(), name='message_create'),
    path('message/delete/<int:pk>/', MessageDeleteView.as_view(), name='message_delete'),
    path('mailing_get/', MailingGetListView.as_view(), name='mailing_get_list'),
    path('mailing_get/<int:pk>/', MailingGetDetailView.as_view(), name='mailing_get_detail'),
    path('mailing_get/update/<int:pk>/', MailingGetUpdateView.as_view(), name='mailing_get_update'),
    path('mailing_get/create/', MailingGetCreateView.as_view(), name='mailing_get_create'),
    path('mailing_get/delete/<int:pk>/', MailingGetDeleteView.as_view(), name='mailing_get_delete'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
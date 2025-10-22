from tempfile import template

from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.views.decorators.cache import cache_page
from .views import MailingGetListView, MailingListView, MessageListView, MessageDetailView, MessageCreateView, \
    MessageDeleteView, MailingCreateView, MessageUpdateView

app_name = 'mailing'

urlpatterns = [
    path('', MailingListView.as_view(), name='mailing_list'),
    path('message/', MessageListView.as_view(), name='message_list'),
    path('message/<int:pk>/', MessageDetailView.as_view(), name='message_detail'),
    path('message/update/<int:pk>/', MessageUpdateView.as_view(), name='message_update'),
    path('message/create/', MessageCreateView.as_view(), name='message_create'),
    path('message/delete/<int:pk>/', MessageDeleteView.as_view(), name='message_delete'),
    path('mailing/create/', MailingCreateView.as_view(), name='mailing_create'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
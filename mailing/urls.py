from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.views.decorators.cache import cache_page
from .views import MailingGetListView

app_name = 'mailing'

urlpatterns = [
    path('', MailingGetListView.as_view(), name='mailing_list'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
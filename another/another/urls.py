from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import TemplateView
from django.urls import path
from polls import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('polls/', include('polls.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.conf.urls import include, url 
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from .views import FileViewSet

router = DefaultRouter()
router.register(r'files', FileViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
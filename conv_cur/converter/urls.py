from django.urls import path

from .views import get_convert

app_name = 'converter'

urlpatterns = [
    path('', get_convert, name='index'),
]

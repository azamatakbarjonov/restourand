from django.urls import path
from .views import test_koment

urlpatterns = [
    path('', test_koment, name='koment'),
]

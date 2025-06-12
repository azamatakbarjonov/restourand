from django.urls import path
from .views import chef_ma

urlpatterns = [
    path('', chef_ma, name='chef'),
]

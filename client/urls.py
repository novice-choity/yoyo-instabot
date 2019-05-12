from django.urls import path

from client import views
from utils.urls.names import (url_client_home, )

urlpatterns = [
    path('', views.ClientHome.as_view(), name=url_client_home),
]

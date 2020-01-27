from django.urls import path

from client import views
from utils.urls.names import (url_client_home, url_client_profile_update, )

urlpatterns = [
    path('', views.ClientHome.as_view(), name=url_client_home),
    path('profile/', views.ClientProfileUpdate.as_view(), name=url_client_profile_update),
]

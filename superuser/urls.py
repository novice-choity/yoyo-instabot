from django.urls import path

from superuser import views
from utils.urls.names import (url_superuser_home, url_superuser_edit_account)

urlpatterns = [
    path('', views.SuperuserHome.as_view(), name=url_superuser_home),
    path('account/', views.EditAccount.as_view(), name=url_superuser_edit_account),

]

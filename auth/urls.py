from django.http import HttpResponseRedirect
from django.urls import path
from django.urls import reverse_lazy

from auth import views
from utils.urls.names import (url_login, url_logout, url_home, url_registration, url_view_home_page,
                              url_registration_success)

urlpatterns = [
    path('', lambda r: HttpResponseRedirect(reverse_lazy(url_login)), name=url_home),
    path('registration/', views.UserRegistrationView.as_view(), name=url_registration),
    path('login/', views.UserLoginView.as_view(), name=url_login),
    path('logout/', views.UserLogoutView.as_view(), name=url_logout),
    path('registration/success/', views.UserRegistrationSuccessView.as_view(), name=url_registration_success),
]

from django.contrib.auth.views import LogoutView, LoginView
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import FormView, TemplateView

from auth.forms import UserLoginForm, UserRegistrationForm
from client.models import Profile, ACTIVE
from utils.helper import get_obj_or_none
from utils.urls.names import (url_login, url_logout, url_superuser_home, url_registration_success, url_client_home)


class UserLoginView(LoginView):
    form_class = UserLoginForm
    template_name = 'auth/login.html'

    def get_user(self):
        return self.request.user

    def get(self, request, *args, **kwargs):
        if self.get_user().is_authenticated:
            return HttpResponseRedirect(self.get_success_url())
        return super().get(request, *args, **kwargs)

    def get_success_url(self):
        user = self.get_user()
        if user and user.is_superuser:
            return reverse_lazy(url_superuser_home)
        elif user and not user.is_superuser:
            active_client = get_obj_or_none(Profile, user=self.request.user, status=ACTIVE)
            if active_client:
                return reverse_lazy(url_client_home)
        #     elif user.user_type == OWNER:
        #         return reverse_lazy(url_owner_view_profile)
        return reverse_lazy(url_logout)


class UserLogoutView(LogoutView):
    next_page = url_login


class UserRegistrationView(FormView):
    template_name = 'auth/register.html'
    form_class = UserRegistrationForm
    success_url = reverse_lazy(url_registration_success)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        form = context.get('form', None)
        return context

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_staff = True
        user.save()
        if user:
            profile = Profile.objects.create(user=user)
        return super().form_valid(form)


class UserRegistrationSuccessView(TemplateView):
    template_name = 'auth/success.html'

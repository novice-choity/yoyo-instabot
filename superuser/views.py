from django.contrib import messages
from django.urls import reverse_lazy
from django.utils.translation import ugettext_lazy as _
from django.views.generic import TemplateView, FormView

from auth.forms import PasswordUpdateForm
from permission.mixins import SuperuserRequiredMixin
from utils.urls.names import url_logout


class SuperuserHome(SuperuserRequiredMixin, TemplateView):
    template_name = 'superuser/home.html'


class EditAccount(SuperuserRequiredMixin, FormView):
    template_name = 'superuser/edit_account.html'
    form_class = PasswordUpdateForm
    success_url = reverse_lazy(url_logout)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        user = form.save(commit=True)
        user.save()
        success_message = _("Password was updated successfully")
        messages.success(self.request, success_message)
        return super().form_valid(form)
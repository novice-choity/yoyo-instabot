from django.views.generic import TemplateView


class RegisterUser(TemplateView):
    template_name = 'auth/register.html'

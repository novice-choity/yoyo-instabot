from django.views.generic import TemplateView

from permission.mixins import ClientRequiredMixin


class ClientHome(ClientRequiredMixin, TemplateView):
    template_name = 'client/home.html'

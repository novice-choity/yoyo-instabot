from django.views.generic import TemplateView

from api_bot import API
from permission.mixins import ClientRequiredMixin


class ClientHome(ClientRequiredMixin, TemplateView):
    template_name = 'client/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        client_api = API()
        login = client_api.login(username='xalien.007', password='Xalien007')
        print(client_api.username)
        print(client_api.rank_token)
        print(client_api.search_location(lat=23.8103, lng=90.4125, query='food'))
        print(client_api.last_json)
        client_api.search_username('xalien')
        print(client_api.last_json)
        return context

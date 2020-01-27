from django.urls import reverse_lazy
from django.views.generic import TemplateView, UpdateView

from api_bot import API
from client.forms import ProfileUpdateForm
from client.models import Profile
from permission.mixins import ClientRequiredMixin
from utils.helper import get_obj_or_none
from utils.urls.names import url_client_home


class ClientHome(ClientRequiredMixin, TemplateView):
    template_name = 'client/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            client_api = API()
            profile = get_obj_or_none(Profile, user=self.request.user)
            # login = client_api.login(username='xalien.007', password='Xalien007')
            login = client_api.login(username=profile.instagram_username, password=profile.instagram_password)
            context.update({'user_name': client_api.username})
            # print(client_api.username)
            # print(client_api.rank_token)
            client_api.search_location(lat=23.8103, lng=90.4125, query='food')
            locations = client_api.last_json
            print(locations)
            # print(client_api.last_json)
            # client_api.search_username('xalien')
            # print(client_api.last_json)
            if locations:
                context['locations'] = locations.get('items')
        except:
            pass
        return context


class ClientProfileUpdate(ClientRequiredMixin, UpdateView):
    model = Profile
    form_class = ProfileUpdateForm
    template_name = 'client/profile.html'
    success_url = reverse_lazy(url_client_home)

    def get_object(self, queryset=None):
        current_user = self.request.user
        return Profile.objects.get(user=current_user)

    def form_valid(self, form):
        profile = form.save(commit=False)
        previous_password = self.get_object().instagram_password
        if profile.instagram_password is None:
            profile.instagram_password = previous_password
        profile.save()
        return super().form_valid(form)

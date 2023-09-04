from django.views.generic import CreateView, ListView, UpdateView
from aplicatie1.models import Location
from django.urls import reverse


class CreateLocationView(CreateView):
    model = Location
    fields = ['city', 'country']
    # fields = '__all__'
    template_name = 'aplicatie1/location_form.html'

    def get_success_url(self):
        return reverse('aplicatie1:lista_locatii')


class UpdateLocationView(UpdateView):
    model = Location
    fields = ['city', 'country']
    # fields = '__all__'
    template_name = 'aplicatie1/location_form.html'

    def get_success_url(self):
        return reverse('aplicatie1:lista_locatii')


class LocationView(ListView):
    model = Location
    template_name = 'aplicatie1/location_index.html'

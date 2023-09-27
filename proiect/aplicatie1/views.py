from django.views.generic import CreateView, ListView, UpdateView

from aplicatie1.forms import LocationClass
from aplicatie1.models import Location, Pontaj
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect
from django.db.models import Q


class CreateLocationView(LoginRequiredMixin, CreateView):
    model = Location
    # fields = ['city', 'country']
    # fields = '__all__'
    form_class = LocationClass
    template_name = 'aplicatie1/location_form.html'

    def form_valid(self, form):
        if form.is_valid():
            location_instance = form.save(commit=False)
            location_instance.user_id = self.request.user.id
            location_instance.save()
        return super(CreateLocationView, self).form_valid(form)

    def get_success_url(self):
        return reverse('aplicatie1:lista_locatii')

    def get_form_kwargs(self):
        data = super(CreateLocationView, self).get_form_kwargs()
        data.update({'pk': None})
        return data

    def get_context_data(self, **kwargs):
        data = super(CreateLocationView, self).get_context_data(*kwargs)
        data['valoare'] = 'Ala bala'
        return data


class UpdateLocationView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Location
    # fields = ['city', 'country']
    # fields = '__all__'
    form_class = LocationClass
    template_name = 'aplicatie1/location_form.html'

    def test_func(self):
        if ((get_location := Location.objects.filter(id=self.kwargs['pk']))
                and get_location.exists()
                and get_location.first().user_id == self.request.user.id):
            return True
        return False

    def get_form_kwargs(self):
        data = super(UpdateLocationView, self).get_form_kwargs()
        data.update({'pk': self.kwargs['pk']})
        return data

    def get_context_data(self, **kwargs):
        data = super(UpdateLocationView, self).get_context_data(*kwargs)
        data['valoare'] = 'Ala bala'
        return data

    def get_success_url(self):
        return reverse('aplicatie1:lista_locatii')


class LocationView(LoginRequiredMixin, ListView):
    model = Location
    template_name = 'aplicatie1/location_index.html'

    def get_context_data(self, *args, **kwargs):
        data = super(LocationView, self).get_context_data(*args, **kwargs)
        if self.request.user.is_superuser:
            data['all_location'] = Location.objects.all()
        else:
            data['all_location'] = Location.objects.filter(user_id=self.request.user.id)
        return data


@login_required
def delete_location(request, pk):
    Location.objects.filter(id=pk, user_id=request.user.id).delete()
    return redirect('aplicatie1:lista_locatii')


@login_required
def deactivate_location(request, pk):
    Location.objects.filter(id=pk, user_id=request.user.id).update(active=0)
    return redirect('aplicatie1:lista_locatii')


@login_required
def activate_location(request, pk):
    Location.objects.filter(id=pk, user_id=request.user.id).update(active=1)
    return redirect('aplicatie1:lista_locatii')


@login_required
def new_timesheet(request):
    Pontaj.objects.create(user_id=request.user.id,
                          start_date=datetime.datetime.now())
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def stop_timesheet(request):
    Pontaj.objects.filter(user_id=request.user.id,
                          end_date=None).update(end_date=datetime.datetime.now())
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

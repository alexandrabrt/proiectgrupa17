from django import forms
from django.forms import TextInput
from aplicatie1.models import Location


class LocationClass(forms.ModelForm):

    class Meta:
        model = Location
        fields = ['city', 'country']

        widgets = {
            'city': TextInput(attrs={'placeholder': "City value", 'class': 'form-control'}),
            'country': TextInput(attrs={'placeholder': "Country value", 'class': 'form-control'}),
        }

    def __init__(self, pk, *args, **kwargs):
        super(LocationClass, self).__init__(*args, **kwargs)
        self.pk = pk

    def clean(self):
        city_value = self.cleaned_data.get('city')
        country_value = self.cleaned_data.get('country')
        if self.pk:
            if Location.objects.filter(city__icontains=city_value, country__icontains=country_value).exclude(id=self.pk).exists():
                self._errors['city'] = self.error_class(['Orasul si tara deja exista'])
        else:
            if Location.objects.filter(city__icontains=city_value, country__icontains=country_value).exists():
                self._errors['city'] = self.error_class(['Orasul si tara deja exista'])
        return self.cleaned_data

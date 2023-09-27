from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, ListView, UpdateView
from django.contrib.auth.models import User
from userprofile.forms import NewAccountForm
from django.urls import reverse
import random
import string
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required


class CreateNewAccountView(LoginRequiredMixin, CreateView):
    model = User
    template_name = 'aplicatie1/location_form.html'
    form_class = NewAccountForm

    def get_form_kwargs(self, **kwargs):
        data = super(CreateNewAccountView, self).get_form_kwargs()
        data.update({'pk': None})
        return data

    def get_success_url(self):
        invite_user(self.object.id)
        return reverse('userprofile:listare_utilizatori')


class ListOfUsersView(LoginRequiredMixin, ListView):
    model = User
    template_name = 'registration/registration_index.html'

    def get_context_data(self, *args, **kwargs):
        data = super(ListOfUsersView, self).get_context_data(*args, **kwargs)
        # data['all_active_users'] = ListOfUsersView.model.objects.filter(is_active=True)
        data['all_active_users'] = self.model.objects.filter(is_active=True)
        return data



class UpdateUserView(LoginRequiredMixin, UpdateView):
    model = User
    template_name = 'aplicatie1/location_form.html'
    form_class = NewAccountForm

    def get_form_kwargs(self, **kwargs):
        data = super(UpdateUserView, self).get_form_kwargs()
        data.update({'pk': self.kwargs['pk']})
        return data

    def get_success_url(self):
        return reverse('userprofile:listare_utilizatori')


def invite_user(user_id):
    psw = ''.join(random.SystemRandom().choice(string.ascii_uppercase +
                                               string.ascii_lowercase +
                                               string.digits + '!$%#@') for _ in range(8))
    if (user_instance := User.objects.filter(id=user_id)) and user_instance.exists():
        user_object = user_instance.first()
        user_object.set_password(psw)
        user_object.save()

        content = f"Buna ziua, \n Datele de autentificare sunt: \n username: {user_object.username} \n parola: {psw}"
        msg_html = render_to_string('registration/invite_user.html', {'content_email': content})
        email = EmailMultiAlternatives(subject='Date contact platforma',
                                       body=content,
                                       from_email='contact@platforma.ro',
                                       to=[user_object.email])
        email.attach_alternative(msg_html, 'text/html')
        email.send()
        return True
    return False


@login_required
def reinvite_user(request, pk):
    if request.user.id != pk:
        invite_user(pk)
    return redirect('userprofile:listare_utilizatori')

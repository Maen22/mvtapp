from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, FormView, ListView
from .forms import CustomUserCreationForm, CustomUserChangeForm, CustomUserForm
from .models import CustomUser


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


class ListUsers(ListView):
    queryset = CustomUser.objects.all()
    template_name = 'ListUsers.html'


class ListPaginateUsers(ListView):
    queryset = CustomUser.objects.all()
    template_name = 'ListPaginateUsers.html'
    paginate_by = 3


class UpdateProfileView(UpdateView):
    form_class = CustomUserForm
    success_url = reverse_lazy('profile')
    template_name = 'profile.html'

    def get_object(self, queryset=None):
        return CustomUser.objects.get(email=self.request.user.email)

    def get_initial(self):
        initial = {
            'email': self.request.user.email,
            'first_name': self.request.user.first_name,
            'last_name': self.request.user.last_name,
        }

        return initial

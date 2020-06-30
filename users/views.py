from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, FormView
from .forms import CustomUserCreationForm, CustomUserChangeForm, CustomUserForm
from .models import CustomUser


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


# @login_required
# def profile(request):
#     return render(request, 'profile.html')


class UpdateProfileView(UpdateView):
    form_class = CustomUserForm
    success_url = reverse_lazy('profile')
    template_name = 'profile.html'

    def get_object(self, queryset=None):
        return CustomUser.objects.get(email=self.request.user.email)

    def get_initial(self):
        # initial = super().get_initial()
        # initial['email'] = self.request.user.email
        # initial['first_name'] = self.request.user.first_name
        # initial['last_name'] = self.request.user.last_name
        initial = {
            'email': self.request.user.email,
            'first_name': self.request.user.first_name,
            'last_name': self.request.user.last_name,
        }

        return initial

from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views import generic
from .models import CustomUser
from .forms import CustomUserCreationForm
from django.shortcuts import render
from django.views.generic import DetailView

class CreateAccountView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'users/createAccount.html'

class UserProfileView(DetailView):
    model = CustomUser
    template_name = 'users/user-profile.html'
    context_object_name = 'account'
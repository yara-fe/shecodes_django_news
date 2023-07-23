from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import CustomUser
from .forms import CustomUserCreationForm, CustomUserChangeForm

class CreateAccountView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login') # The `reverse_lazy` function is used to provide the success URL as a string
    template_name = 'users/createAccount.html'

class UserProfileView(LoginRequiredMixin, DetailView, UpdateView):
    model = CustomUser
    form_class = CustomUserChangeForm
    template_name = 'users/user-profile.html'
    success_url = reverse_lazy('news:index')

    def get_object(self, queryset=None):
        # Use the captured 'pk' from the URL to fetch the specific user's profile
        return self.model.objects.get(pk=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = self.get_form()
        return context

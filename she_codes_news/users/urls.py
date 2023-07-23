from django.urls import path
from .views import CreateAccountView, UserProfileView
from . import views

app_name = 'users'

urlpatterns = [
    path('create-account/', CreateAccountView.as_view(), name='createAccount'),
    path('<int:pk>/user-profile/', UserProfileView.as_view(), name='user-profile'),
]
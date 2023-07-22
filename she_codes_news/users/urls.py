from django.urls import path
from .views import CreateAccountView
from . import views

app_name = 'users'

urlpatterns = [
    path('create-account/', CreateAccountView.as_view(), name='createAccount'),
    path('<int:pk>/user-profile', views.UserProfileView.as_view(), name='user-profile'),
]
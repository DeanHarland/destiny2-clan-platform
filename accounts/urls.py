from django.contrib.auth.views import LoginView
from django.urls import path, include
from . import views
from .forms import CustomAuthenticationForm

urlpatterns = [
    path('register/', views.register, name='register'),
    path('profile/', views.profile_view, name='profile'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),

    path(
        'login/',
        LoginView.as_view(
            template_name='registration/login.html',
            authentication_form=CustomAuthenticationForm,
        ),
        name='login',
    ),

    # django built-in auth (login/logout)
    path('', include('django.contrib.auth.urls')),
    path('profile/', views.profile_view, name='profile'),


]
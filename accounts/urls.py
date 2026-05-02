from django.urls import path, include
from . import views

urlpatterns = [
    # your custom views
    path('register/', views.register, name='register'),
    path('profile/', views.profile_view, name='profile'),

    # django built-in auth (login/logout)
    path('', include('django.contrib.auth.urls')),
]
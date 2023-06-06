from django.urls import path
from django.contrib.auth.views import (
    LoginView,
    LogoutView,
)

from .views import (
    SignUpView,
    profile_redirect,
    create_profile,
    profile,
    get_trips,
    get_country_origin
)

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('profile_redirect/', profile_redirect, name='profile_redirect'),
    path('create_profile/', create_profile, name='create_profile'),
    path('profile/<int:profile_id>', profile, name='profile'),
    path('api/get_trips/<int:profile_id>', get_trips, name='get_trips'),
    path('api/get_origin/<int:profile_id>', get_country_origin, name='get_trips'),
]

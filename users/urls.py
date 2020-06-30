from django.contrib.auth.decorators import login_required
from django.urls import path
from .views import SignUpView, UpdateProfileView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('profile/', login_required(UpdateProfileView.as_view()), name='profile'),
]

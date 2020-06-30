from django.contrib.auth.decorators import login_required
from django.urls import path
from .views import SignUpView, UpdateProfileView, ListUsers, ListPaginateUsers

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('profile/', login_required(UpdateProfileView.as_view()), name='profile'),
    path('users-list/', login_required(ListUsers.as_view()), name='users-list'),
    path('users-list-paginate/', login_required(ListPaginateUsers.as_view()), name='users-list-paginate'),
]

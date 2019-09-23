from django.urls import path
from django.contrib.auth.views import LogoutView
from accounts.views import AccountsLoginView, SignupFormView, ProfileView


urlpatterns = [
    path('login/', AccountsLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page = '/'), name='logout'),
    path('signup/', SignupFormView.as_view(), name='signup'),
    path('profile/', ProfileView.as_view(), name='profile'),
]

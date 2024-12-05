from django.urls import path
from django.contrib.auth.views import LoginView
from .views import RegisterView, MyLogoutView

app_name = 'accounts'

urlpatterns = [
    path('login/',
         LoginView.as_view(
             template_name='accounts/login.html',
             redirect_authenticated_user=True
         ), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('logout/', MyLogoutView.as_view(), name='logout'),
]

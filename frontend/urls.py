from django.urls import path
from .views import landing_page, login_page, signup_page, home_page

urlpatterns = [
    path('', landing_page, name='landing_page'),
    path('login/', login_page, name='login_page'),
    path('signup/', signup_page, name='signup_page'),
    path('home/', home_page, name='home_page'),
]
from django.urls import path, include
from users.views import *

urlpatterns = [
    path('', homepage, name = 'homepage'),
    path('dashboard', dashboard, name = 'dashboard'),
    path('signin', signin, name = 'signin'),
    path('signup', signup, name = 'signup'),
    path('signout', signout, name = 'signout'),
    path('resetpass', resetpass, name = 'resetpass'),
]
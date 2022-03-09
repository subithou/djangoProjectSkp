from django.urls import include, path
import login, home
from user.views import user_home

urlpatterns = [
    path('', user_home, name='user_home'),

]

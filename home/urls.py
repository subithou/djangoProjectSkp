from django.urls import include, path
from home.views import dashboard
import login, home


urlpatterns = [
    path('', dashboard, name='dashboard'),

]

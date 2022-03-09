from django.urls import include, path
import login, home
from login.views import login_page

urlpatterns = [
    path('', login_page, name='login_page'),

]

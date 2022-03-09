from django.urls import include, path
import login, home
from login.views import add_auction, auction, live_auction, login_page

urlpatterns = [
    path('', login_page, name='login_page'),
    path('auction/', auction, name='auction_page'),
    path('add_auction/ <p_id>', add_auction, name='add_auction'),
    path('live_auction/', live_auction, name='live_auction'),

]

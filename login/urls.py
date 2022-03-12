from django.urls import include, path
import login, home
from login.views import add_auction, auction, live_auction, login_page, cancel_auction, view_players

urlpatterns = [
    path('', login_page, name='login_page'),
    path('auction/', auction, name='auction_page'),
    path('add_auction/ <p_id>', add_auction, name='add_auction'),
    path('cancel_auction/ <p_id>', cancel_auction, name='cancel_auction'),

    path('view_players/ <team_name>', view_players, name='view_players'),
    path('live_auction/', live_auction, name='live_auction'),

]

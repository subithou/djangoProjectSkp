from unicodedata import name
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib import messages
from home.models import auction_data, profile, team
import login
from login.models import auction_admin

# Create your views here.
def login_page(request):
    if request.method == 'POST':
        uname =  request.POST.get('username')
        pswrd = request.POST.get('password')
        print(uname, pswrd)
        data = auction_admin.objects.filter(username=uname, password=pswrd)
        if data :
            return redirect(login.views.auction)
        else:
            return render(request,'login.html')
    return render(request,'login.html')

def auction(request):
    team_details = team.objects.all()
    prqofile_details = profile.objects.all()
    return render(request, 'auction.html', {'team_details': team_details, 'profile_data': prqofile_details})

def add_auction(request, p_id):
    print(p_id)
    profile_data = profile.objects.get(player_id=p_id)
    team_data = team.objects.all()
    for i in team_data:
        team_count = team.objects.filter(name=i).count()
        
    p1_data = profile.objects.get(player_id=p_id)
    p1_data.active = 1
    p1_data.save()

    if request.method == 'POST':
        team_name = request.POST.get('team_name')
        amount = request.POST.get('amount')
        team_details = team.objects.get(name=team_name)
        team_amount = team_details.balance_amount
        check_auction_done = auction_data.objects.filter(player_id=p_id)
        

        if check_auction_done:
            messages.error(request, 'Player already added')
        else:

            if int(amount) <= team_amount:
                team_details.balance_amount = team_amount - int(amount)
                team_details.save()

                p_data = profile.objects.get(player_id=p_id)
                p_data.team = team_name
                p_data.amount = int(amount)
                p_data.active = 0
                p_data.save()

                auction_data.objects.create(player_id=p_id, team=team_name, amount=int(amount))

                return redirect(login.views.auction)
            else:
                messages.error(request, 'Insufficient balance')


    return render(request, 'add_auction.html', {'profile_data': profile_data, 'team_data': team_data})

def cancel_auction(request, p_id):
    p_data = profile.objects.get(player_id=p_id)
    p_data.active = 0
    p_data.save()
    return redirect(login.views.auction)
                
def live_auction(request):
    team_details = team.objects.all()
    auction_data1 = auction_data.objects.all()
    profile_data = profile.objects.all()
    auction_profile = profile.objects.filter(active=1)
    for i in auction_profile:
        print(i)
    return render(request, 'live_auction.html', {'team_details':team_details, 'auction_data':auction_data1, 'profile_data':profile_data,
                                                'auction_profile':auction_profile})
            
def view_players(request, team_name):
    team_details = team.objects.filter(name=team_name)
    prqofile_details = profile.objects.filter(team=team_name)
    return render(request, 'team_players.html', {'team_details': team_details, 'profile_data': prqofile_details})
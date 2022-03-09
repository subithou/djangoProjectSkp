from multiprocessing import context
from django.shortcuts import render

from home.models import profile, team

# Create your views here.
def user_home(request):
    team_details = team.objects.all()
    prqofile_details = profile.objects.all()
    return render(request, 'user.html', {'team_details': team_details, 'profile_data': prqofile_details})
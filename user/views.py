from multiprocessing import context
from django.shortcuts import render

from home.models import team

# Create your views here.
def user_home(request):
    team_details = team.objects.filter()
    return render(request, 'user.html', {'context': team_details})
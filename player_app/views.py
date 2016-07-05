from django.shortcuts import render
from django.http import HttpResponse
import requests
from bs4 import BeautifulSoup


def get_stats(request):
    hostname = 'http://www.nfl.com'
    player = request.GET.get('player') or 'cam newton'  # retrieving from html input
    status = request.GET.get('historical') or 'current'
    content = requests.get(hostname + '/players/search?category=name&filter={}&playerType={}'.format(player, status)).text
    souper = BeautifulSoup(content, "html.parser")
    url = hostname + (souper.find(id='result').a.attrs['href'])  # creating a new url
    content = requests.get(url)
    souper = BeautifulSoup(content.text, "html.parser")
    bio = str(souper.find(id='player-bio'))
    profile = str(souper.find(id='player-stats-wrapper'))
    return render(request, 'index.html', {'profile': profile, 'player': player, 'bio': bio})

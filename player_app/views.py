from django.shortcuts import render
from django.http import HttpResponse
import requests
from bs4 import BeautifulSoup

#
# def get_player_stats(request):
#     return HttpResponse("howdy")



def player_stats_view(request):
    content = requests.get('http://www.nfl.com/players/search?category=name&filter=staubach&playerType=historical')
    souper = BeautifulSoup(content, "html.parser")
    print(dir(content))

    # souper = BeautifulSoup(content, "html.parser")
    # print("Feels like: ", souper.find(id='curFeel').text)  # this delivers 88 F
    # print("Real temp: ", souper.find(id='curTemp').text)  # this delivers 88 F

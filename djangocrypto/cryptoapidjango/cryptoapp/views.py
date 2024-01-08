import requests
from django.shortcuts import render
from django.conf import settings
# Create your views here.
def index(request):
    # fetching data
    apidata = requests.get('https://api.coingecko.com/api/v3/coins/markets?vs_currency=USD&order=market_cap_desc&per_page=100&page=1&sparkline=false ').json()
    # we have our data in apidata variable..let's pass this to our index.html file show fetched data
    return render(request,'index.html',{'apidata':apidata})





 

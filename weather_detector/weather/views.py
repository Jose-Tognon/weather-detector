from django.shortcuts import render
import requests
from dotenv import load_dotenv
import os
# Create your views here.
load_dotenv()

def index(request):
    template_name = 'index.html'
    if request.method == "POST":
        api_key = os.getenv('API_KEY')
        city = request.POST['city']
        print(city)
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
        res = requests.get(url)
        data = {
            "country_code": res.json()['sys']['country'],
            "coordinate": f'Longitude: {res.json()['coord']['lon']} / Latitude: {res.json()['coord']['lat']}',
            "temp": str(round((res.json()['main']['temp']) - 273.15,2)) + " °C",
            "pressure": res.json()['main']['pressure'],
            "humidity": res.json()['main']['humidity'],
            "city":city,
        }
    else:
        data = {}     
    return render(request,template_name,data)
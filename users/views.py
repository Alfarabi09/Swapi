from django.shortcuts import render
import requests

def index(request):
    context = {}
    if 'fetch_data' in request.POST:
        response = requests.get('https://swapi.dev/api/people/')
        context['characters'] = response.json()['results']
    return render(request, 'users/index.html', context)
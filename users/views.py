from django.shortcuts import render
import requests
from django.core.cache import cache

def home_view(request):
    return render(request, 'users/home.html')

def get_people(request):
    context = {}
    if 'fetch_data' in request.POST:
        characters = cache.get('characters')

        if not characters:
            characters = []
            url = 'https://swapi.dev/api/people/'
            while url:
                try:
                    response = requests.get(url, timeout=5)
                    response.raise_for_status()  
                    data = response.json()
                    characters.extend(data['results'])
                    url = data['next']
                except requests.RequestException as e:
                    print(f"Ошибка запроса: {e}")  
                    break

            cache.set('characters', characters, timeout=3600)  

        context['characters'] = characters
    return render(request, 'users/people.html', context)

def get_planets(request):
    context = {}
    if 'fetch_data' in request.POST:
        planets = cache.get('planets')

        if not planets:
            planets = []
            url = 'https://swapi.dev/api/planets/'
            while url:
                try:
                    response = requests.get(url, timeout=5)
                    response.raise_for_status()
                    data = response.json()
                    planets.extend(data['results'])
                    url = data['next']
                except requests.RequestException as e:
                    print(f"Ошибка запроса: {e}")
                    break

            cache.set('planets', planets, timeout=3600)

        context['planets'] = planets
    return render(request, 'users/planets.html', context)

def get_starships(request):
    context = {}
    if 'fetch_data' in request.POST:
        starships = cache.get('starships')

        if not starships:
            starships = []
            url = 'https://swapi.dev/api/starships/'
            while url:
                try:
                    response = requests.get(url, timeout=5)
                    response.raise_for_status()
                    data = response.json()
                    starships.extend(data['results'])
                    url = data['next']
                except requests.RequestException as e:
                    print(f"Ошибка запроса: {e}")
                    break
                
            cache.set('starships', starships, timeout=3600)

        context['starships'] = starships
    return render(request, 'users/starships.html', context)
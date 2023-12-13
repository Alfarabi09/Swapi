from django.urls import path
from .views import get_people, home_view, get_planets, get_starships

app_name = 'users'

urlpatterns = [
    path('', home_view, name='home'),
    path('people', get_people, name='people'),
    path('planets', get_planets, name='planets'),
    path('starships/', get_starships, name='starships'),
]

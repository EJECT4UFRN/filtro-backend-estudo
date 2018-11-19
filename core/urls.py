from django.urls import path
from core.views import home, pesquisa, home_javascript, pesquisa_javascript

urlpatterns = [
    path('', home),
    path('pesquisa/', pesquisa),
    path('home-javascript/', home_javascript),
    path('pesquisa/curso/<str:nome>', pesquisa_javascript),
]
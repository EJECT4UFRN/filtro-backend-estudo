from django.urls import path
from core.views import home, pesquisa

urlpatterns = [
    path('', home),
    path('pesquisa/', pesquisa),
]
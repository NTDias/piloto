from django.urls import path
from . import views

urlpatterns = [
    path('', index, name='index'),  # (aspas vazias = página inicial)
    path('sobre/', sobre, name='sobre'),
    path('contato/', contato, name='contato'),  
    path('ajuda/', ajuda, name='ajuda'),
]
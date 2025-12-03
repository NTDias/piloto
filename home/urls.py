from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # (aspas vazias = página inicial)
    path('sobre/', views.sobre, name='sobre'),
    path('contato/', views.contato, name='contato'),  
    path('ajuda/', views.ajuda, name='ajuda'),
]
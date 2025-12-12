from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('sobre/', views.sobre, name='sobre'),
    path('contato/', views.contato, name='contato'),
    path('ajuda/', views.ajuda, name='ajuda'),
    path('produto/', views.produto, name='produto'),
    path('item/<int:id>', views.exibir_item, name='exibir_item'),
    path('diasemana/<int:dia>', views.dia_semana, name='dia_semana'),
    path('home/', views.home, name='home'),
    path('produto/form', views.form_produto, name='form_produto'),
    
]

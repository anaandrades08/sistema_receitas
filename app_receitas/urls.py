from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('inicio/', views.inicio, name='inicio'),
    path('quemsomos/', views.quemsomos, name='quemsomos'),
    path('contato/', views.contato, name='contato'),
    path('login/', views.login, name='login'),
    path('politicaprivacidade/', views.politicaprivacidade, name='politicaprivacidade'),
]
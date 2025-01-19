from django.urls import path
from . import views


urlpatterns = [
    path('', views.sabor, name='sabor'),
    path('receita/<slug>/', views.receita, name='receita'),
]
from django.urls import path
from . import views


urlpatterns = [
    path('', views.cadastros, name='cadastro'),
    path('login', views.logviu, name='login'),
    path('receitas', views.sabor, name='sabor'),
    path('receita/<slug>/', views.receita, name='receita'),

]

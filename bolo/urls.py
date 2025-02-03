from django.urls import path
from . import views


urlpatterns = [
    path('', views.cadastros, name='cadastro'),
    path('login', views.logviu, name='login'),
    path('receitas', views.sabor, name='receitas'),
    path('postagem', views.postagem, name='postagem'),
    path('receita/<slug>/<int:pk>', views.receita, name='receita'),

]

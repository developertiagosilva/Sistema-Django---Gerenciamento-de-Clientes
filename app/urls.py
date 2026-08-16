from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    # Configura o logout para redirecionar direto para a tela de login após sair
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('clientes/', views.clientes, name='clientes'),
    path('cadastrar/', views.cadastrar, name='cadastrar'),
]
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('nossosistema/', views.nossosistema, name='nosso-sistema'),
    path('planos/', views.planos, name='planos'),
    path('login/', views.login, name='login'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard/morador/<int:id>', views.dadosMorador, name='dados-morador'),
    path('dashboard/novomorador/', views.novoMorador, name='novo-morador'),
    path('dashboard/editmorador/<int:id>', views.editMorador, name='edit-morador'),
    path('dashboard/deletemorador/<int:id>', views.deleteMorador, name='delete-morador'),
]

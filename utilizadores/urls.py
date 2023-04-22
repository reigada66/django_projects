from django.urls import path
from . import views
from django.contrib.auth import views as auth_views



urlpatterns = [
    path('registar', views.registar, name='registar'),
    path('perfil/', views.perfil, name='perfil'),
    path('login/', auth_views.LoginView.as_view(template_name='utilizadores/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='utilizadores/logout.html'), name='logout'),
    path('mudapass/', auth_views.PasswordChangeView.as_view(template_name='urilizadores/mudapass.html'), name='mudapass'),
    path('activate/<uidb64>/<token>', views.activate, name='activate'),

]
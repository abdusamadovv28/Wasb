from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.index, name='index'),
    path('logic/', views.logic, name='logic'),
    path('work/', views.work, name='work'),
    path('about/', views.about, name='about'),
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout_view, name='logout'),
]

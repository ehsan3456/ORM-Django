from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    #path('login/', views.login_user, name='home'),
    path('logout/', views.logout_user, name='logout'),
    #path('', views.home, name='home'),
]

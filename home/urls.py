from django.contrib import admin
from django.urls import path,include
from . import views



urlpatterns = [
    path("",views.home,name="home"),
    path('overview', views.overview, name="overview" ),
    path('contact', views.cont, name="contact" ),
    path('contribute', views.contribute, name="contribute" ),
    path('join', views.join, name="join" ),
    path('vision', views.vision, name="vision" ),
    path('founder', views.founder, name="founder" ),
    path('awards', views.awards, name="awards" ),
    path('team', views.team, name="team" ),
    path('signup',views.signup,name="signup"),
    path('login',views.login,name="login"),
    path('logout',views.logout,name="logout"),
   
]
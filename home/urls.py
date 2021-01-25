from django.contrib import admin
from django.urls import path
from home import views


urlpatterns =[
    path('', views.index, name='home'),
    path('contact', views.contact, name='contact'),
    path('about', views.about, name='about'),
    path('gold', views.gold, name='gold'),
    path('diamond', views.diamond, name='diamond'),
    path('silver', views.silver, name='silver'),

    
]

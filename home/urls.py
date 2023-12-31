"""
URL configuration for BookMyGround project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    # if request with empty path then send to views.index and set path name as 'home'
    path('', views.signup, name='signup'),
    path('home', views.home, name='home'),
    path('pune', views.pune, name='pune'),
    path('pune1', views.pune1, name='pune1'),
    path('contact', views.contact, name='contact'),
    path('login', views.login, name='login'),
    path('payment', views.payment, name='payment'),
    path('book', views.book, name='book'),
    path('logout/', views.LogoutPage, name='logout'),
]

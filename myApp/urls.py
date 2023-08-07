from django.contrib import admin
from django.urls import path
from myApp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', views.register,name='register'),
    path('login/', views.login, name='login'),
    path('', views.home, name='home'),
    path('course/', views.course,name='courses' ),
    path('aboutus/', views.aboutus, name='aboutus'),
    path('main/', views.main, name='mainpage')
]

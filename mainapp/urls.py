from mainapp import views
from django.urls import path
from mainapp.apps import MainappConfig

app_name = MainappConfig.name

urlpatterns = [
    path('', views.home, name='home'),
    path('password/', views.password, name='password'),
    path('description/', views.description, name='description')
]

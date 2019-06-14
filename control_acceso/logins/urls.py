from logins import views
from django.conf.urls import url
from django.urls import path

app_name = 'miapp'

urlpatterns = [
    path('', views.index,name='index'),
    path('login/', views.login,name='login'),
    path('registro/', views.registro,name='registro'),
]

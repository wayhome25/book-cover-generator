from django.urls import path

from cover import views

app_name = 'cover'

urlpatterns = [
    path('index/', views.index, name='index'),
]

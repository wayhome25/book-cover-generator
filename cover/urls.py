from django.urls import path

from cover import views

app_name = 'cover'

urlpatterns = [
    path('index/', views.index, name='index'),
    path('image.png/', views.image_generator, name='image_generator'),
]

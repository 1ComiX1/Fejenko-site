from django.urls import path

from . import views


app_name = 'core'
urlpatterns = [
    path('', views.index, name='index'),
    path('services/', views.services, name='services'),
    path('aboutme/', views.aboutme, name='aboutme'),
    path('confidentiality/', views.confidentiality, name='confidentiality'),
    path('portfolio/', views.portfolio, name='portfolio'),
]
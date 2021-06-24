from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('services/', views.service, name='service'),
    path('skills/', views.skill, name='skill'),
    path('contact/', views.contact, name='contact')
]
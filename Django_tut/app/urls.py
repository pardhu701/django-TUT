from django.urls import path
from . import views

urlpatterns = [
    path('', views.members, name='members'),
    path('mem', views.mem, name='mem'),
    path('',views.prac, name='praca'),
]
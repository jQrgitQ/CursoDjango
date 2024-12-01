from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('testing/', views.testing, name='testing'),
    path('members/', views.members, name='members'),
    path('members/details/<int:id>', views.details, name='details'),

]



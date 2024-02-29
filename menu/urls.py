from django.urls import path
from . import views

urlpatterns = [
    path('<slug:food_slug>/', views.food_detail, name='food_detail'), 
]
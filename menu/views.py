from django.shortcuts import render

# Create your views here.
from django.shortcuts import get_object_or_404,render
from .models import FoodItem
from .recommendations import get_recommendations


def show_recommendations(request,food_title):
    recommendations = get_recommendations(food_title)

    return render(request, 'food/recommendation.html', {'recommendations': recommendations})

def food_detail(request, food_slug):
    food = get_object_or_404(FoodItem, slug=food_slug)

    # Get recommendations for the current food item
    recommendations = get_recommendations(food.food_title)

    context = {
        'food': food,
        'recommendations': recommendations,
    }

    return render(request, 'food/food.html', context)
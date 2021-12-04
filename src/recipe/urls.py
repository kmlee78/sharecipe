from django.urls import path
from . import views

app_name = "recipe"

urlpatterns = [
    path('create_recipe', views.create_recipe_view, name= "create_recipe"),
    path('create_ingredients', views.create_ingredients_view, name="create_ingredients"),
    path('create_methods', views.create_methods_view, name= "create_methods"),
    path('create_theme', views.create_theme_view, name= "create_theme"),
]
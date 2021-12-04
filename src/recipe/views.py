from django.shortcuts import render
from django.shortcuts import redirect
from . models import Recipe
from django.db import connection

def create_recipe_view(request):
    if request.method == "POST":
        name = request.POST["name"]
        user = request.user
        with connection.cursor() as cursor:
            cursor.execute("""
            INSERT INTO recipe_Recipe (name) VALUES('{}');
            """.format(name))
        return redirect("recipe:create_ingredients")
    return render(request, "recipe/recipe.html")

def create_ingredients_view(request):
    if request.method == "POST":
        name = request.POST["name"]
        quantity = request.POST["quantity"]
        cursor = connection.cursor()
        cursor.execute("""
        SELECT id FROM recipe_Recipe
        WHERE id=(
            SELECT max(id) FROM recipe_Recipe
        )
        """)
        result = cursor.fetchall()
        cursor.execute("""
        INSERT INTO recipe_Ingredients (name, quantity, recipe_id)
        VALUES('{}', '{}', '{}');
        """.format(name, quantity, result[0][0]))
    return render(request, "recipe/ingredients.html")

def create_methods_view(request):
    if request.method == "POST":
        name = request.POST["name"]
        time = request.POST["time"]
        cursor = connection.cursor()
        cursor.execute("""
        SELECT max(id) FROM recipe_Recipe
        """)
        result = cursor.fetchall()
        cursor.execute("""
        INSERT INTO recipe_Methods (name, time, recipe_id)
        VALUES('{}', '{}', '{}');
        """.format(name, time, result[0][0]))
    return render(request, "recipe/methods.html")

def create_theme_view(request):
    if request.method == "POST":
        name = request.POST["name"]
        cursor = connection.cursor()
        cursor.execute("""
        SELECT max(id) FROM recipe_Recipe
        """)
        result = cursor.fetchall()
        cursor.execute("""
        INSERT INTO recipe_Theme (name, recipe_id)
        VALUES('{}', '{}');
        """.format(name, result[0][0]))
    return render(request, "recipe/theme.html")



# Create your views here.

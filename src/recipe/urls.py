from django.urls import path
from recipe import views

urlpatterns = [
    # path("", views.api_root),
    path("recipes/", views.RecipeList.as_view()),
    path("recipes/<int:recipe_id>/", views.RecipeDetail.as_view()),
    path("recipes/<int:recipe_id>/reviews", views.ReviewList.as_view()),
    path("reviews/all/", views.ReviewAll.as_view()),
    path(
        "reviews/<int:review_id>/",
        views.ReviewDetail.as_view(),
    ),
    path("ingredients/", views.IngredientList.as_view()),
    path("methods/", views.MethodList.as_view()),
    path("themes/", views.ThemeList.as_view()),
]

# urlpatterns = format_suffix_patterns(urlpatterns)

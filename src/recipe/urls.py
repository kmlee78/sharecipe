from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    # path("", views.api_root),
    path("users/", views.UserList.as_view()),
    path("users/<int:pk>/", views.UserList.as_view()),
    path("recipes/", views.RecipeList.as_view()),
    path("recipes/<int:pk>/", views.RecipeDetail.as_view()),
    path("reviews/", views.ReviewList.as_view()),
    path("reviews/<int:pk>/", views.ReviewDetail.as_view()),
]

# urlpatterns = format_suffix_patterns(urlpatterns)

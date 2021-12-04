from django.urls import path
from user import views

urlpatterns = [
    path("users/signup/", views.SignUpView.as_view()),
    path("users/", views.UserListView.as_view()),
    path("users/<int:pk>/", views.UserDetailView.as_view()),
]

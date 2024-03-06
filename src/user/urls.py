from django.urls import path

from .views import MeView, UserListCreateView, UserRetrieveUpdateDestroyView

urlpatterns = [
    path("me/", MeView.as_view(), name="me"),
    path("users/", UserListCreateView.as_view(), name="user"),
    path("users/<str:pk>/", UserRetrieveUpdateDestroyView.as_view(), name="user_detail"),
]

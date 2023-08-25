from django.urls import path
from .views import DetailWindowAPIView, WindowAPIView, UserWindowsListView

urlpatterns = [
    path('product/', WindowAPIView.as_view()),
    path('product/<id>/', DetailWindowAPIView.as_view()),
    path('user/<str:username>/windows/', UserWindowsListView.as_view()),
]

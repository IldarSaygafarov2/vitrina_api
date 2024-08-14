from django.urls import path
from . import views

urlpatterns = [
    path('', views.users_api_root),
    path('<str:tg_username>/type/', views.UserTypeRetrieveView.as_view())
]
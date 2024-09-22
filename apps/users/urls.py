from django.urls import path
from . import views

from rest_framework_nested import routers




urlpatterns = [
    # path('', views.users_api_root),
    path('list/', views.UserListView.as_view()),
    path('<str:tg_username>/type/', views.UserTypeRetrieveView.as_view()),
    path('<str:tg_username>/user/', views.UserIdRetrieveView.as_view()),
]
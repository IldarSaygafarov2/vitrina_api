from django.urls import path
from rest_framework_nested import routers

from . import views

router = routers.DefaultRouter()
router.register(r'', views.UserListView)

urlpatterns = [
    path('<int:pk>/advertisements/', views.RealtorAdvertisementListView.as_view()),
    path('<str:tg_username>/type/', views.UserTypeRetrieveView.as_view()),
    path('<str:tg_username>/user/', views.UserIdRetrieveView.as_view()),

]

urlpatterns += router.urls

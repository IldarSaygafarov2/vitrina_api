from django.urls import path
from . import views
from rest_framework_nested import routers

router = routers.DefaultRouter()
router.register(r'categories', views.CategoryViewSet)
router.register(r'advertisements', views.AdvertisementViewSet)



urlpatterns = [

]


urlpatterns += router.urls
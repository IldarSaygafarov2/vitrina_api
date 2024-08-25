from django.urls import path
from rest_framework_nested import routers

from . import views

router = routers.DefaultRouter()
router.register(r'categories', views.CategoryViewSet)
router.register(r'advertisements', views.AdvertisementViewSet)
router.register(r'districts', views.DisrtrictViewSet)

urlpatterns = [

]

urlpatterns += router.urls

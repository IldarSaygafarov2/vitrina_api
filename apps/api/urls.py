from django.urls import path
# from rest_framework_nested import routers
from rest_framework_nested import routers

from . import views

router = routers.DefaultRouter()
router.register(r'categories', views.CategoryViewSet)
router.register(r'advertisements', views.AdvertisementViewSet)
router.register(r'districts', views.DisrtrictViewSet)

advertisement_router = routers.NestedDefaultRouter(router, 'advertisements', lookup='advertisement')
advertisement_router.register('gallery', views.AdvertisementGalleryView)

urlpatterns = [
    path('request/add/', views.UserRequestCreateView.as_view()),
]

urlpatterns += router.urls + advertisement_router.urls

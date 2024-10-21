from django.urls import path
from rest_framework_nested import routers

from . import views

router = routers.DefaultRouter()
router.register(r'', views.UserListView)
# router.register('advertisement_moderation', views.RealtorAdvertisementOnModerationView)


realtor_advertisement_moderation_router = routers.NestedDefaultRouter(
    router,
    r'',
    lookup='user'
)
realtor_advertisement_moderation_router.register('moderation_advertisements',
                                                 views.RealtorAdvertisementOnModerationView,
                                                 basename='moderation_advertisements')

urlpatterns = [
    path('<int:pk>/advertisements/', views.RealtorAdvertisementListView.as_view()),
    path('<str:tg_username>/type/', views.UserTypeRetrieveView.as_view()),
    path('<str:tg_username>/user/', views.UserIdRetrieveView.as_view()),
]

urlpatterns += router.urls + realtor_advertisement_moderation_router.urls

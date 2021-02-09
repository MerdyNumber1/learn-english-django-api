from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from rest_framework.routers import DefaultRouter

from .views import UserViewSet


router = DefaultRouter()
router.register('', UserViewSet, basename='user')

urlpatterns = [
    path('token/', jwt_views.TokenObtainPairView.as_view(), name='get token'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token refresh'),
    *router.urls
]

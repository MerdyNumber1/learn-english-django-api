from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from rest_framework.routers import SimpleRouter

from .views import UserViewSet


router = SimpleRouter(trailing_slash=False)
router.register('', UserViewSet, basename='user')

urlpatterns = [
    path('token/', jwt_views.TokenObtainPairView.as_view(), name='get token'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token refresh'),
    *router.urls
]

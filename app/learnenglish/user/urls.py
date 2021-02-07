from django.urls import path
from rest_framework_simplejwt import views as jwt_views

from .views import UserCreate

urlpatterns = [
    path('', UserCreate.as_view(), name='create_user'),
    path('token/', jwt_views.TokenObtainPairView.as_view(), name='get token'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token refresh'),
]

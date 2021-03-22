from django.contrib import admin
from django.urls import path, re_path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="Learn English",
        default_version='v1',
    ),
    public=True,
    permission_classes=(permissions.AllowAny, ),
)

urlpatterns = [
    re_path(
        r'^swagger/$',
        schema_view.with_ui('swagger', cache_timeout=0),
        name='schema-swagger-ui',
    ),
    path('admin/', admin.site.urls),
    path('users/', include('profile.urls')),
    path('', include('practice.urls')),
    path('', include('theory.urls'))
]

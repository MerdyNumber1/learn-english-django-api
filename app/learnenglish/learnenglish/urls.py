from django.contrib import admin
from django.urls import path, re_path, include


urlpatterns = [
    re_path(r'^docs/', include('rest_framework_docs.urls')),
    path('admin/', admin.site.urls),
    path('users/', include('user.urls'))
]

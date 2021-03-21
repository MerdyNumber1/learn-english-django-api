from rest_framework.routers import SimpleRouter

from .views import ExerciseViewSet

router = SimpleRouter()
router.register(r'exercises', ExerciseViewSet, basename='practice')

urlpatterns = [
    *router.urls,
]

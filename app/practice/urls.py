from rest_framework.routers import SimpleRouter

from .views import ExerciseViewSet, ExerciseReportViewSet

router = SimpleRouter()
router.register(r'exercises', ExerciseViewSet, basename='practice-exercise')
router.register(r'reports', ExerciseReportViewSet, basename='practice-report')

urlpatterns = [
    *router.urls,
]

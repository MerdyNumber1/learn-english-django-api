from rest_framework.routers import SimpleRouter

from .views import TopicViewSet, ArticleViewSet

router = SimpleRouter()
router.register(r'topics', TopicViewSet, basename='theory-topic')
router.register(r'articles', ArticleViewSet, basename='theory-article')

urlpatterns = [
    *router.urls,
]

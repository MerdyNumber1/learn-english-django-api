from rest_framework import viewsets
from rest_framework import permissions

from .models import Topic, Article
from .serializers import TopicDetailSerializer, ArticleDetailSerializer


class TopicViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = TopicDetailSerializer
    queryset = Topic.objects.all()
    permissions_classes = [permissions.IsAuthenticated]


class ArticleViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = ArticleDetailSerializer
    queryset = Article.objects.all()
    permissions_classes = [permissions.IsAuthenticated]



from rest_framework import viewsets
from rest_framework import permissions

from .models import Message
from .serializers import MessageSerializer


class MessageViewSet(viewsets.ReadOnlyModelViewSet, viewsets.mixins.CreateModelMixin):
    serializer_class = MessageSerializer
    queryset = Message.objects.all()
    permissions_classes = [permissions.IsAuthenticated]


from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import User
from .serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    @action(
        detail=False,
        methods=['GET'],
        url_path='me',
        permission_classes=[permissions.IsAuthenticated],
    )
    def current_user(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)

    def get_permissions(self):
        if self.action == 'create':
            return [permissions.AllowAny()]

        return super().get_permissions()

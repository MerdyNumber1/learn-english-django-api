from rest_framework import viewsets
from rest_framework import permissions

from .models import Exercise
from .serializers import ExerciseSerializer


class ExerciseViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = ExerciseSerializer
    queryset = Exercise.objects.all()
    permissions_classes = [permissions.IsAuthenticated]

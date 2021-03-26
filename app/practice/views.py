from rest_framework import viewsets
from rest_framework import permissions

from .models import Exercise, ExerciseReport
from .serializers import ExerciseSerializer, ExerciseReportSerializer


class ExerciseViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = ExerciseSerializer
    queryset = Exercise.objects.all()
    permissions_classes = [permissions.IsAuthenticated]


class ExerciseReportViewSet(viewsets.ModelViewSet):
    serializer_class = ExerciseReportSerializer
    queryset = ExerciseReport.objects.all()
    permission_classes = [permissions.IsAuthenticated]


from rest_framework import viewsets
from rest_framework import permissions

from .models import Exercise, ExerciseReport
from .serializers import ExerciseDetailSerializer, ExerciseReportDetailSerializer, ExerciseReportCreationSerializer


class ExerciseViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = ExerciseDetailSerializer
    queryset = Exercise.objects.all()
    permissions_classes = [permissions.IsAuthenticated]


class ExerciseReportViewSet(viewsets.ModelViewSet):
    queryset = ExerciseReport.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return ExerciseReportDetailSerializer

        return ExerciseReportCreationSerializer

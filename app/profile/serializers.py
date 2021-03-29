from rest_framework import serializers

from . import services as user_service
from .models import User
from .dto import UserDTO


class UserSerializer(serializers.ModelSerializer):
    registration_date = serializers.ReadOnlyField()
    correct_reports_count = serializers.SerializerMethodField()

    def get_correct_reports_count(self, user) -> int:
        return len(user_service.get_user_correct_reports(user.id))

    class Meta:
        model = User
        fields = ('id', 'email', 'username', 'password', 'registration_date', 'correct_reports_count')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data: UserDTO) -> User:
        return user_service.create_user(validated_data)

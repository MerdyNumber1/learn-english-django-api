from typing import List

from .models import User
from .dto import UserDTO

from practice.models import ExerciseReport


def create_user(user_data: UserDTO) -> User:
    return User.objects.create_user(user_data)


def create_superuser(user_data: UserDTO) -> User:
    return User.objects.create_superuser(user_data)


def get_user_correct_reports(user_id: int) -> List[ExerciseReport]:
    return [report for report in ExerciseReport.objects.filter(user__id=user_id).all() if report.is_correct]

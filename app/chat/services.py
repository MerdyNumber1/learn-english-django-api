from django.shortcuts import get_object_or_404

from practice.models import Exercise
from theory.models import Article

from .models import Message


def create_message(data, user):
    message_type = data.get('type')
    exercise = None
    article = None

    if message_type == 'exercise_reply':
        exercise = get_object_or_404(Exercise, id=data.get('exercise_id'))
    elif message_type == 'article_reply':
        article = get_object_or_404(Article, id=data.get('article_id'))

    return Message.objects.create(
        message=data.get('message'),
        user=user,
        type=message_type,
        exercise=exercise,
        article=article
    )

from .models import Message


def create_message(data, user):
    message_type = data.get('type', 'message')
    article = None
    exercise = None

    if message_type == Message.MessageType.ARTICLE_REPLY:
        article = data.get('article')
    elif message_type == Message.MessageType.EXERCISE_REPLY:
        exercise = data.get('exercise')

    return Message.objects.create(
        message=data.get('message'),
        type=message_type,
        article=article,
        exercise=exercise,
        user=user,
    )

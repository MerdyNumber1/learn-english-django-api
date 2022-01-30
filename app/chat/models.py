from django.db import models

from profile.models import User
from theory.models import Article
from practice.models import Exercise


class Message(models.Model):
    class MessageType(models.TextChoices):
        MESSAGE = 'message'
        ARTICLE_REPLY = 'article_reply'
        EXERCISE_REPLY = 'exercise_reply'

    message = models.TextField(verbose_name='сообщение')
    type = models.CharField(max_length=14, choices=MessageType.choices, default=MessageType.MESSAGE)

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='messages', verbose_name='Пользователь')
    article = models.ForeignKey(Article, null=True, on_delete=models.CASCADE, related_name='messages', verbose_name='Статья')
    exercise = models.ForeignKey(Exercise, null=True, on_delete=models.CASCADE, related_name='messages', verbose_name='Упражнение')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'сообщение'
        verbose_name_plural = 'сообщения'
        ordering = ('created_at',)

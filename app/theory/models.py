from django.db import models


class Topic(models.Model):
    title = models.CharField(max_length=200, verbose_name='название')
    description = models.CharField(max_length=20000, blank=True, verbose_name='описание')

    class Meta:
        verbose_name = 'тема'
        verbose_name_plural = 'темы'

    def __str__(self) -> str:
        return str(self.title)


class Article(models.Model):
    title = models.CharField(max_length=200, verbose_name='название')
    content = models.CharField(max_length=100000, verbose_name='содержание')
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name='articles', verbose_name='тема')

    class Meta:
        verbose_name = 'статья'
        verbose_name_plural = 'статьи'

    def __str__(self) -> str:
        return str(self.title)

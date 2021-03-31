from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from .models import Topic, Article


class TopicAdmin(SummernoteModelAdmin):
    summernote_fields = ('description',)


class ArticleAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)
    list_display = ('title', 'get_topic_title')

    def get_topic_title(self, article):
        return article.topic.title

    get_topic_title.short_description = 'тема'


admin.site.register(Topic, TopicAdmin)
admin.site.register(Article, ArticleAdmin)

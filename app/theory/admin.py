from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from .models import Topic, Article


class TopicAdmin(SummernoteModelAdmin):
    summernote_fields = ('description',)


class ArticleAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)


admin.site.register(Topic, TopicAdmin)
admin.site.register(Article, ArticleAdmin)

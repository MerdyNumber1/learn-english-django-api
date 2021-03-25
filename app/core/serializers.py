from rest_framework import serializers


class StringPrimaryKeyRelatedField(serializers.RelatedField):
    def to_representation(self, value):
        return {'id': value.id, 'title': str(value)}

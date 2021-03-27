from typing import Dict
from rest_framework import serializers


class StringPrimaryKeyRelatedField(serializers.RelatedField):

    def to_representation(self, value) -> Dict[str, str]:
        return {'id': value.id, 'title': str(value)}

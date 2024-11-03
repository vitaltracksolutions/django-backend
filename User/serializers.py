from rest_framework.serializers import ModelSerializer
from Snippet.models import Snippet
class SnippetSerializer(ModelSerializer):
    class Meta:
        model = Snippet
        fields = ['id', 'name', 'gender', 'age', 'occupation']
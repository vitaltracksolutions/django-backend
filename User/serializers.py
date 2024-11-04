from rest_framework.serializers import ModelSerializer
from User.models import Info
class InfoSerializer(ModelSerializer):
    class Meta:
        model = Info
        fields = ['id', 'name', 'gender', 'age', 'occupation']
from .models import CustomUser
from rest_framework.serializers import HyperlinkedModelSerializer


class CustomUserModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["username", "first_name", "last_name", "email"]

from rest_framework.viewsets import ModelViewSet
from .models import CustomUser
from .serializers import CustomUserModelSerializer, CustomUserModelSerializerWithStatus


class CustomUserModelViewSet(ModelViewSet):
    queryset = CustomUser.objects.all().order_by("-is_superuser")
    serializer_class = CustomUserModelSerializer
    http_method_names = ['get', 'put']

    def get_serializer_class(self):
        if self.request.version == "0.1":
            return CustomUserModelSerializerWithStatus
        return CustomUserModelSerializer

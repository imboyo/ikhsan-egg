from rest_framework.viewsets import ModelViewSet

from .models import Egg
from .serializers import EggSerializer


# Create your views here.
class EggViewSet(ModelViewSet):
    queryset = Egg.objects.all()
    serializer_class = EggSerializer
    ordering_fields = ['-created_at']


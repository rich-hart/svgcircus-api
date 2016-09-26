from .models import Circle
from rest_framework import viewsets
from .serializers import CircleSerializer

class CircleViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Circle.objects.all()
    serializer_class = CircleSerializer


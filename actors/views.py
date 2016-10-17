from .models import (
    Actor, 
    Color,
    Position,
)
from rest_framework import viewsets
from .serializers import (
    ActorSerializer, 
    ColorSerializer,
    PositionSerializer,
)

class ActorViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer

class ColorViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Color.objects.all()
    serializer_class = ColorSerializer

class PositionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Position.objects.all()
    serializer_class = PositionSerializer


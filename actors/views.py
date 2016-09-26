from .models import Actor
from rest_framework import viewsets
from .serializers import ActorSerializer

class ActorViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


from rest_framework import viewsets

from crud.models import State
from crud.serializers import StateSerializer

# Create your views here.
class StatesViewSet(viewsets.ModelViewSet):
    queryset = State.objects.all()
    serializer_class = StateSerializer

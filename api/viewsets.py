from rest_framework import viewsets
from api import serializers
from api import models

class MembroViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.MembroSerializer
    queryset = models.Membro.objects.all()
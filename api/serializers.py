from rest_framework import serializers
from api import models

class MembroSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Membro
        fields = '__all__'
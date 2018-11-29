from rest_framework import serializers
from .models import Mascota, Usuario

class MascotaSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'all'
        )
        model = Mascota
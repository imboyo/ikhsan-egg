from rest_framework import serializers
from .models import Egg


class EggSerializer(serializers.ModelSerializer):
    class Meta:
        model = Egg
        fields = [
            'id',
            'total',
            'good',
            'not_good',
            'created_at',
        ]
        read_only_fields = ['id']

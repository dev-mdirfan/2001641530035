# numbers/serializers.py
from rest_framework import serializers
from .models import MergedNumbers

class MergedNumbersSerializer(serializers.ModelSerializer):
    class Meta:
        model = MergedNumbers
        fields = ['numbers']

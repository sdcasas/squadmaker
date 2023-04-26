from rest_framework import serializers

from apps.joker.models import Joker


class JokerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Joker
        fields = '__all__'
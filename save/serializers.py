from django.db import IntegrityError
from rest_framework import serializers
from save.models import Save


class SaveSerializer(serializers.ModelSerializer):
    """Serializer for the Save model"""
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Save()
        fields = [
            'id', 'created_on', 'owner', 'walk_post']

    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                'detail': 'possible duplicate'
            })


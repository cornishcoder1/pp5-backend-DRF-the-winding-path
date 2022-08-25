from rest_framework import serializers
from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    """Profile serializer to convert Django model instances to JSON"""
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        """Method to check if request.user is the same as owner"""
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        """Meta class to to specify model and fields"""
        model = Profile
        fields = [
            'id', 'owner', 'created_on', 'updated_on', 'name', 'city',
            'location', 'bio', 'image', 'is_owner',
        ]

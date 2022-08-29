from rest_framework import serializers
from .models import Profile
from followers.models import Follower


class ProfileSerializer(serializers.ModelSerializer):
    """Profile serializer to convert Django model instances to JSON"""
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    following_id = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        """Method to check if request.user is the same as owner"""
        request = self.context['request']
        return request.user == obj.owner

    def get_following_id(self, obj):
        """Method to return following count for individual user"""
        user = self.context['request'].user
        if user.is_authenticated:
            following = Follower.objects.filter(
                owner=user, followed=obj.owner
            ).first()
            # print(following)
            return following.id if following else None
        return None

    class Meta:
        """Meta class to to specify model and fields"""
        model = Profile
        fields = [
            'id', 'owner', 'created_on', 'updated_on', 'name', 'city',
            'location', 'bio', 'image', 'is_owner', 'following_id',
        ]

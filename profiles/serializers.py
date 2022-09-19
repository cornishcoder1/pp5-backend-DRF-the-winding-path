from rest_framework import serializers
from .models import Profile
from followers.models import Follower


class ProfileSerializer(serializers.ModelSerializer):
    """Profile serializer to convert Django model instances to JSON"""
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    following_id = serializers.SerializerMethodField()
    walk_posts_count = serializers.ReadOnlyField()
    gallery_posts_count = serializers.ReadOnlyField()
    followers_count = serializers.ReadOnlyField()
    following_count = serializers.ReadOnlyField()

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
            return following.id if following else None
        return None

    class Meta:
        """Meta class to to specify model and fields"""
        model = Profile
        fields = [
            'id', 'owner', 'created_on', 'updated_on', 'name', 'city',
            'location', 'bio', 'image', 'is_owner', 'following_id',
            'walk_posts_count', 'gallery_posts_count', 'followers_count',
            'following_count',
        ]

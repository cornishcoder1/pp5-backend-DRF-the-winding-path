from rest_framework import serializers
from .models import Post
from save.models import Save


class PostSerializer(serializers.ModelSerializer):
    """Post serializer to convert Django model instances to JSON"""
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    save_id = serializers.SerializerMethodField()

    def validate_image(self, value):
        "Check values for size, width and height on post images"
        if value.size > 1024 * 1024 * 2:
            raise serializers.ValidationError(
                'Image size larger than 2MB!'
            )
        if value.image.width > 4096:
            raise serializers.ValidationError(
                'Image width larger than 4096px'
            )
        if value.image.height > 4096:
            raise serializers.ValidationError(
                'Image height larger than 4096px'
            )
        return value

    def get_is_owner(self, obj):
        """Method to check if request.user is the same as owner"""
        request = self.context['request']
        return request.user == obj.owner

    def get_save_id(self, obj):
        """Method to return saves count for individual user"""
        user = self.context['request'].user
        if user.is_authenticated:
            saved = Save.objects.filter(
                owner=user, walk_post=obj
            ).first()
            return saved.id if saved else None
        return None

    class Meta:
        """Meta class to to specify model and fields"""
        model = Post
        fields = [
            'id',
            'owner',
            'is_owner',
            'profile_id',
            'profile_image',
            'created_on',
            'updated_on',
            'title',
            'headline',
            'image',
            'environment',
            'wc',
            'dog_friendly',
            'difficulty',
            'length',
            'duration',
            'content',
            'save_id',
        ]

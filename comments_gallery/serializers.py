from django.contrib.humanize.templatetags.humanize import naturaltime
from rest_framework import serializers
from comments_gallery.models import GalleryComment


class GalleryCommentSerializer(serializers.ModelSerializer):
    """
    Serializer for the Gallery Comment model
    Adds three extra fields when returning a list of Comment instances
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    created_on = serializers.SerializerMethodField()
    updated_on = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        """Method to check if request.user is the same as owner"""
        request = self.context['request']
        return request.user == obj.owner

    def get_created_on(self, obj):
        """Method to display when comment was posted"""
        return naturaltime(obj.created_on)

    def get_updated_on(self, obj):
        """Method to display when comment was updated"""
        return naturaltime(obj.updated_on)

    class Meta:
        """Meta class to to specify model and fields"""
        model = GalleryComment
        fields = [
            'id', 'owner', 'is_owner', 'profile_id', 'profile_image',
            'gallery_post', 'created_on', 'updated_on', 'content'
        ]


class GalleryCommentDetailSerializer(GalleryCommentSerializer):
    """
    Serializer for the Gallery Comment model used in Detail view
    """
    gallery_post = serializers.ReadOnlyField(source='gallery_post.id')

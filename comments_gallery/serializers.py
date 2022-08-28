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
        request = self.context['request']
        return request.user == obj.owner

    def get_created_at(self, obj):
        return naturaltime(obj.created_at)

    def get_updated_at(self, obj):
        return naturaltime(obj.updated_at)

    class Meta:
        model = GalleryComment
        fields = [
            'id', 'owner', 'is_owner', 'profile_id', 'profile_image',
            'gallery_post', 'created_on', 'updated_on', 'content'
        ]


class CommentDetailSerializer(GalleryCommentSerializer):
    """
    Serializer for the Gallery Comment model used in Detail view
    """
    gallery_post = serializers.ReadOnlyField(source='gallery_post.id')

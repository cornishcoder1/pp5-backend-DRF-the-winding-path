from rest_framework import serializers
from .models import Contact


class ContactSerializer(serializers.ModelSerializer):
    """Contact serializer to convert Django model instances to JSON"""

    class Meta:
        """Meta class to to specify model and fields"""
        model = Contact
        fields = [
            'fname',
            'lname',
            'email',
            'content',
            'created_on',
        ]

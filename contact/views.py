from rest_framework import generics
from .models import Contact
from .serializer import ContactSerializer


class ContactDetail(generics.ListCreateAPIView):
    """Allows user to submit contact form"""
    serializer_class = ContactSerializer
    queryset = Contact.objects.all()


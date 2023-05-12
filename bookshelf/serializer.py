from rest_framework import serializers
from .models import Book
from accounts.serializer import UserSerializer

class BookSerializer(serializers.ModelSerializer):
    user = UserSerializer
    class Meta:
        model = Book
        fields = '__all__'
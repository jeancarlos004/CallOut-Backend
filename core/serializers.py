from rest_framework import serializers
from .models import BlockedCall

from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class ChatSerializer(serializers.Serializer):
    message = serializers.CharField()
    response = serializers.CharField(read_only=True)

class BlockedCallSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlockedCall
        fields = '__all__'
        extra_kwargs = {'user': {'read_only': True}}

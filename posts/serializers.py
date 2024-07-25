from rest_framework import serializers
from .models import Post
from django.contrib.auth.models import User

class PostSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'user', 'username', 'content', 'image', 'aura', 'created_at']
        read_only_fields = ['user', 'username', 'created_at']

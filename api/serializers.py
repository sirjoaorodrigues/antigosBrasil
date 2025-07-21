# api/serializers.py
from rest_framework import serializers
from django.contrib.auth.models import User
from social.models import Post, Comments

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'date_joined']

class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    
    class Meta:
        model = Comments
        fields = ['id', 'user', 'text', 'post']

class PostSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    comments = CommentSerializer(many=True, read_only=True)
    comments_count = serializers.SerializerMethodField()
    
    class Meta:
        model = Post
        fields = ['id', 'user', 'text', 'image', 'comments', 'comments_count']
    
    def get_comments_count(self, obj):
        return obj.comments.count()

# Serializers for creating posts and comments
class PostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['text', 'image']

class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = ['text', 'post']
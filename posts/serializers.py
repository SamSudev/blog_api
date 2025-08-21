# posts/serializers.py

from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'publication_date', 'author']
        # No necesitamos read_only_fields para el autor
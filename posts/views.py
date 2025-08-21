from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from .models import Post
from .serializers import PostSerializer

class PostViewSet(viewsets.ModelViewSet):
    """
    Un ViewSet para ver y editar entradas de blog.
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
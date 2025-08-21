# posts/views.py

from rest_framework import viewsets
from rest_framework.permissions import AllowAny # Importa AllowAny
from .models import Post
from .serializers import PostSerializer

class PostViewSet(viewsets.ModelViewSet):
    """
    Un ViewSet para ver y editar entradas de blog.
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [AllowAny] # Permite el acceso a cualquier usuario
    
    # Ya no necesitas el método perform_create
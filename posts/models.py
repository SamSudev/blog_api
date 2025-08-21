from django.db import models

# Create your models here.
# posts/models.py

from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
 #ENTRADAS DEL POST
 
    title = models.CharField(max_length=200, verbose_name="Título")
    content = models.TextField(verbose_name="Contenido")
    publication_date = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de publicación")
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="posts",
        verbose_name="Autor"
    )

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-publication_date']
        verbose_name = "Entrada de Blog"
        verbose_name_plural = "Entradas de Blog"
# posts/models.py

from django.db import models
# Ya no necesitamos importar 'User' si el autor es un string

class Post(models.Model):
    """
    Modelo para las entradas del blog.
    """
    title = models.CharField(max_length=200, verbose_name="Título")
    content = models.TextField(verbose_name="Contenido")
    publication_date = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de publicación")
    author = models.CharField(max_length=100, verbose_name="Autor") # Campo de texto para el autor

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-publication_date']
        verbose_name = "Entrada de Blog"
        verbose_name_plural = "Entradas de Blog"
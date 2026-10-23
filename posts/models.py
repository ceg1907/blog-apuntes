from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    CATEGORIAS = [
        ('python', 'Python'),
        ('javascript', 'JavaScript'),
        ('html_css', 'HTML/CSS'),
        ('git', 'Git'),
    ]

    titulo = models.CharField(max_length=150)
    contenido = models.TextField()
    imagen = models.ImageField(upload_to='posts/', blank=True, null=True)
    categoria = models.CharField(max_length=20, choices=CATEGORIAS)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='posts_con_like', blank=True)

    class Meta:
        ordering = ['-fecha_creacion']

    def __str__(self):
        return self.titulo

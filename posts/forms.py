from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['titulo', 'categoria', 'contenido', 'imagen']
        labels = {
            'titulo': 'Título del apunte',
            'categoria': 'Categoría',
            'contenido': 'Contenido',
            'imagen': 'Imagen de portada',
        }
        widgets = {
            'titulo': forms.TextInput(attrs={
                'placeholder': 'Ej: Entendiendo los arrays en JavaScript',
            }),
            'contenido': forms.Textarea(attrs={
                'placeholder': 'Contá qué aprendiste, agregá ejemplos y compartí tus consejos...',
                'rows': 10,
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['categoria'].choices = [('', 'Elegí una categoría')] + Post.CATEGORIAS
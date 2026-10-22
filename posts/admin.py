from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'categoria', 'autor', 'fecha_creacion')
    list_filter = ('categoria',)

# Register your models here.

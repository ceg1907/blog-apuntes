from django.views.generic import ListView, DetailView
from .models import Post


class PostListView(ListView):
    model = Post
    template_name = 'posts/post_list.html'
    context_object_name = 'posts'

    def get_queryset(self):
        posts = super().get_queryset()
        categoria = self.request.GET.get('categoria')
        if categoria:
            posts = posts.filter(categoria=categoria)
        return posts


class PostDetailView(DetailView):
    model = Post
    template_name = 'posts/post_detail.html'
    context_object_name = 'post'

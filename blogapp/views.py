from django.shortcuts import get_object_or_404, render

from .models import Post
from django.views.generic import ListView


class PostListView(ListView):
    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 2
    template_name = "blog/post/list.html"


def post_detail(request, slug):
    post = get_object_or_404(Post, status="published", slug=slug)
    return render(request, 'blog/post/detail.html', {'post': post})

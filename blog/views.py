from django.views import generic

from .models import Post

# Create your views here.


class PostList(generic.ListView):
    """ A view to return a list of all blog posts """

    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'blog/blog.html'


class PostDetail(generic.DetailView):
    """ A view to return the detail of a blog post """

    model = Post
    template_name = 'blog/post_detail.html'

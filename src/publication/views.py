from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from publication.models import BlogPost
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


def accueil_page(request):
    return render(request, "accueil.html")

class BlogHome(ListView):
    model = BlogPost
    context_object_name = "posts"
    template_name = "posts/blogpost_all.html"

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.is_authenticated:
            return queryset
        
        return queryset.filter(published=True)
    

@method_decorator(login_required, name='dispatch')
class BlogPostCreate(CreateView):
    model = BlogPost
    template_name = "posts/blogpost_create.html"
    fields = ['title', 'content', 'published', 'author', ]
    
    
@method_decorator(login_required, name='dispatch')
class BlogPostUpdate(UpdateView):
    model = BlogPost
    template_name = "posts/blogpost_update.html"
    fields = ['title', 'content', 'published', 'author', ]


class BlogPostDetail(DetailView):
    model = BlogPost
    context_object_name = "post"
    template_name = "posts/blogpost_detail.html"
    
    
@method_decorator(login_required, name='dispatch')
class BlogPostDelete(DeleteView):
    model = BlogPost
    template_name = "posts/blogpost_delete.html"
    context_object_name = "post"
    success_url = reverse_lazy("posts:home")

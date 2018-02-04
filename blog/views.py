from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, FormView
from .models import Article, Comment
from .forms import BlogForm, CommentForm
# Create your views here.

class BlogListView(ListView):
    model = Article
    template_name = "blog/home.html"

class BlogDetailView(DetailView):
    model = Article
    template_name = "blog/detail.html"

class BlogCreateView(CreateView):
    model = Article
    form_class = BlogForm
    template_name = "blog/form.html"
    success_url = "/"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(BlogCreateView, self).form_valid(form)


class AddComment(LoginRequiredMixin, FormView):
    login_url = "login"
    model = Comment
    form_class = CommentForm
    template_name = "blog/comment.html"
    success_url = "blog_detail_view"

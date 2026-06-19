# from django.views.generic import ListView, DetailView
# from django.views.generic.edit import CreateView, UpdateView,DeleteView
# from django.urls import reverse_lazy
# from .models import Post
# class BlogListView(ListView):
#     model = Post
#     template_name = "home.html"
# class BlogDetailView(DetailView):
#     model = Post
#     template_name = "post_detail.html"

# class BlogCreateView(CreateView):
#     model = Post
#     template_name = "post_new.html"
#     fields = ["title", "author", "body"]

# class BlogUpdateView(UpdateView):
#     model = Post
#     template_name = "post_edit.html"
#     fields = ["title", "body"]

# class BlogDeleteView(DeleteView):
#     model = Post
#     template_name = "post_delete.html"
#     success_url = reverse_lazy("home")


from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin,
)

from django.urls import reverse_lazy

from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

from .models import Post


class BlogListView(ListView):
    model = Post
    template_name = "home.html"


class BlogDetailView(DetailView):
    model = Post
    template_name = "post_detail.html"


class BlogCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = "post_new.html"
    fields = ["title", "body"]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class BlogUpdateView(
    LoginRequiredMixin,
    UserPassesTestMixin,
    UpdateView,
):
    model = Post
    template_name = "post_edit.html"
    fields = ["title", "body"]

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author


class BlogDeleteView(
    LoginRequiredMixin,
    UserPassesTestMixin,
    DeleteView,
):
    model = Post
    template_name = "post_delete.html"
    success_url = reverse_lazy("home")

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author


class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = "registration/signup.html"
    success_url = reverse_lazy("login")






#FUnction based views
# from django.shortcuts import render, get_object_or_404
# from .models import Post

# def post_list(request):
#     posts = Post.objects.all()
#     return render(request, 'home.html', {'posts': posts})

# def post_detail(request, pk): # new
#     post = get_object_or_404(Post, pk=pk)
#     return render(request, "post_detail.html", {"post": post})'
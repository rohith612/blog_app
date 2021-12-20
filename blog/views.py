from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import View
from django.views.generic import ListView, DetailView
from .models import Comment, Post
from .forms import CommentForm

# index/home page view
class StartingPageView(ListView):
    template_name = "blog/index.html"
    model = Post
    ordering = ["-date"]
    context_object_name = "posts"

    # this is override the model operation on query
    # Post.objects.all()[:3]
    def get_queryset(self):
        queryset = super().get_queryset()
        data = queryset[:3]
        return data

# all item page view
class AllPostView(ListView):
    template_name = "blog/all_posts.html"
    model = Post
    ordering = ["-date"]
    context_object_name = "all_posts"

# content detail page view 
class SinglePostView(View):

    def get(self, request, slug):
        post = Post.objects.get(slug=slug)
        context = {
            "post" : post,
            "post_tags" : post.tags.all(),
            "comment_form" : CommentForm(),
            "comments" : post.comments.all().order_by("-id")
        }
        return render(request, 'blog/post_detail.html', context)
        

    def post(self, request, slug):
        comment_form = CommentForm(request.POST)
        post = Post.objects.get(slug=slug)

        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
            return HttpResponseRedirect(reverse("post_detail_page", args=[slug]))
        
        context = {
            "post" : post,
            "post_tags" : post.tags.all(),
            "comment_form" : comment_form,
            "comments" : post.comments.all().order_by("-id")
        }
        return render(request, 'blog/post_detail.html', context)

        # def get_context_data(self, **kwargs):
        #     context = super().get_context_data(**kwargs)
        #     context["post_tags"] = self.object.tags.all() 
        #     context["comment_form"] = CommentForm()
        #     return context

class ReadLaterView(View):

    def get(self, request):
        stored_posts = request.session.get('stored_posts')
        context = {}
        if stored_posts is None or len(stored_posts) == 0:
            context["posts"] = []
            context["has_post"] = False
        else:
            context["posts"] = Post.objects.filter(id__in=stored_posts) # WHERE IN clause
            context["has_post"] = True

        return render(request, "blog/stored_posts.html", context)

    def post(self, request):
        stored_posts = request.session.get('stored_posts')
        if stored_posts is None:
            stored_posts = []
        
        post_id = int(request.POST["post_id"])
        if post_id not in stored_posts:
            stored_posts.append(post_id)
            request.session['stored_posts'] = stored_posts

        return HttpResponseRedirect("/")



        


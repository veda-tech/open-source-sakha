from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import CreateView, DetailView, ListView

from .forms import CommentForm, PostForm
from .models import Forum, Post, Topic


class ForumListPage(ListView):
    queryset = Forum.objects.all()
    template_name = "forum_app/forum-list.html"


class TopicListPage(ListView):
    queryset = Topic.objects.all()
    template_name = "forum_app/forum-topics.html"

    def get_context_data(self, *args, **kwargs):
        data = super().get_context_data(*args, **kwargs)
        data["forum"] = get_object_or_404(Forum, pk=self.kwargs["forum_pk"])
        return data

    def get_queryset(self):
        return super().get_queryset().filter(forum_id=self.kwargs["forum_pk"])


class PostListPage(ListView):
    queryset = Post.objects.all()
    template_name = "forum_app/forum-posts.html"

    def get_context_data(self, *args, **kwargs):
        data = super().get_context_data(*args, **kwargs)
        data["forum"] = get_object_or_404(Forum, pk=self.kwargs["forum_pk"])
        data["topic"] = get_object_or_404(Topic, pk=self.kwargs["topic_pk"])
        return data

    def get_queryset(self):
        return super().get_queryset().filter(topic_id=self.kwargs["topic_pk"])


class PostDetailPage(DetailView):
    queryset = Post.objects.all().prefetch_related("comment_set")
    template_name = "forum_app/forum-post-detail.html"

    def get_context_data(self, *args, **kwargs):
        data = super().get_context_data(**kwargs)
        data["forum"] = get_object_or_404(Forum, pk=self.kwargs["forum_pk"])
        data["topic"] = get_object_or_404(Topic, pk=self.kwargs["topic_pk"])
        return data


class PostCreatePage(CreateView):
    form_class = PostForm
    template_name = "forum_app/forum-post-create.html"

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


@login_required
def add_comment(request, pk, *args, **kwargs):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect(
                reverse(
                    "post-detail",
                    kwargs={
                        "topic_pk": post.topic_id,
                        "forum_pk": post.topic.forum_id,
                        "pk": post.uuid,
                    },
                )
            )
    return redirect(reverse("forum_app-post-detail", kwargs={"pk": post.uuid}))

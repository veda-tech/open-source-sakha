from django.urls import path

from forum_app.views import (
    PostDetailPage,
    PostListPage,
    ForumListPage,
    TopicListPage,
    PostCreatePage,
    add_comment,
)

urlpatterns = [
    path("", ForumListPage.as_view(), name="forum-list"),
    path("post/create", PostCreatePage.as_view(), name="post-create"),
    path("<forum_pk>", TopicListPage.as_view(), name="topic-list"),
    path("<forum_pk>/<topic_pk>", PostListPage.as_view(), name="post-list"),
    path(
        "<forum_pk>/<topic_pk>/<pk>",
        PostDetailPage.as_view(),
        name="post-detail",
    ),
    path(
        "<forum_pk>/<topic_pk>/<pk>/add_comment",
        add_comment,
        name="post-add-comment",
    ),
]

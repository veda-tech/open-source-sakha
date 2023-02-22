from django.contrib.auth import get_user_model
from django.db import models

from core.models import AbstractModel

User = get_user_model()


class Forum(AbstractModel):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f"/forums/{self.uuid}"

    class Meta:
        ordering = ["name"]


class Topic(AbstractModel):
    title = models.CharField(max_length=100)
    forum = models.ForeignKey(Forum, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.forum.name}-{self.title}"

    def get_absolute_url(self):
        return f"/forums/{self.forum_id}/{self.uuid}"

    class Meta:
        ordering = ["forum__name"]


class Post(AbstractModel):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f"/forums/{self.topic.forum_id}/{self.topic_id}/{self.uuid}"


class Comment(AbstractModel):
    content = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ["-created"]

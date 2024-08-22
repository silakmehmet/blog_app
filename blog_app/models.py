from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name}"


class Blog(models.Model):
    STATUS = (
        ('d', 'Draft'), ('p', 'Published')
    )

    title = models.CharField(max_length=60, unique=True)
    content = models.TextField()
    image = models.CharField(max_length=150)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="blog_category")
    publish_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_user")
    status = models.CharField(choices=STATUS)

    def __str__(self):
        return f"{self.category} - {self.title}"


class PostViews(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user_postviews")
    post_views = models.BooleanField(default=False)
    blog = models.ForeignKey(
        Blog, on_delete=models.CASCADE, related_name="post_blog")
    time_stamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Post Views"
        verbose_name_plural = "Post Views"

    def __strt__(self):
        return f"Views by {self.user} on {self.blog}"


class Comment(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, related_name="user_comment")
    time_stamp = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    content = models.CharField(max_length=255)
    blog = models.ForeignKey(
        Blog, on_delete=models.CASCADE, related_name="comment_blog")

    def __str__(self):
        return f"Comment by {self.user} on {self.blog}"


class Likes(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="like_user")
    blog = models.ForeignKey(
        Blog, on_delete=models.CASCADE, related_name="like_blog")
    likes = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Likes"
        verbose_name_plural = "Likes"

    def __str__(self):
        return f"Like by {self.user} on {self.blog}"

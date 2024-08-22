from django.contrib.auth.models import User

from rest_framework import serializers

from .models import Category, Blog, PostViews, Comment, Likes


class CategorySerializer(serializers.ModesSerializer):
    class Meta:
        model = Category
        fields = "__all__"
        read_only_fields = ["id"]


class BlogSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    user = serializers.ReadOnlyField(source="user.username")

    class Meta:
        model = Blog
        fields = "__all__"
        read_only_fields = ["id", "category"]


class CommentSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source="user.username")
    blog = serializers.PrimaryKeyRelatedField(queryset=Blog.objects.all())

    class Meta:
        model = Comment
        fields = "__all__"
        read_only_fields = ["id", "blog"]


class PostViewsSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source="user.username")
    blog = serializers.PrimaryKeyRelatedField(queryset=Blog.objects.all())

    class Meta:
        model = PostViews
        fields = "__all__"
        read_only_fields = ["id", "blog"]


class LikesSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source="user.username")
    blog = serializers.PrimaryKeyRelatedField(queryset=Blog.objects.all())

    class Meta:
        model = Likes
        fields = "__all__"
        read_only_fields = ["id", "blog"]

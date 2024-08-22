from rest_framework.viewsets import ModelViewSet

from .models import Category, Blog, PostViews, Comment, Likes
from .serializers import CategorySerializer, BlogSerializer, PostViewsSerializer, CommentSerializer, LikesSerializer


class CategoryMVS(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class BlogMVS(ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer


class PostViewsMVS(ModelViewSet):
    queryset = PostViews.objects.all()
    serializer_class = PostViewsSerializer


class CommentMVS(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class LikesMVS(ModelViewSet):
    queryset = Likes.objects.all()
    serializer_class = LikesSerializer

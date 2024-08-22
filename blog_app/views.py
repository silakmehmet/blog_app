from rest_framework.viewsets import ModelViewSet

from .models import Category, Blog, PostViews, Comment, Likes
from .serializers import CategorySerializer, BlogSerializer, PostViewsSerializer, CommentSerializer, LikesSerializer


class CategoryMVS(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class BlogMVS(ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class PostViewsMVS(ModelViewSet):
    queryset = PostViews.objects.all()
    serializer_class = PostViewsSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CommentMVS(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class LikesMVS(ModelViewSet):
    queryset = Likes.objects.all()
    serializer_class = LikesSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

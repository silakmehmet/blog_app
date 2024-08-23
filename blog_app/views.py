from django.contrib.auth.models import User

from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from .models import Category, Blog, PostViews, Comment, Likes
from .serializers import CategorySerializer, BlogSerializer, UserBlogSerializer, PostViewsSerializer, CommentSerializer, LikesSerializer
from .permissions import IsAdminOrReadOnly, IsOwnerOrAdminOrReadOnly, IsOwnerOrReadOnly


class CategoryMVS(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminOrReadOnly]


class BlogMVS(ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [IsOwnerOrAdminOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            if user.is_staff:
                # Admins see all blogs
                return Blog.objects.all()
            else:
                # Regular users see their own drafts and published blogs
                return Blog.objects.filter(user=user) | Blog.objects.filter(status='p')
        else:
            # Non-authenticated users see only published blogs
            return Blog.objects.filter(status='p')

    def get_serializer_class(self):
        if self.request.user.is_staff:
            return UserBlogSerializer
        return BlogSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)

        # Create a PostView entry when the blog detail is retrieved
        if request.user.is_authenticated:
            PostViews.objects.create(user=request.user, blog=instance)
        else:
            # Handling unauthenticated users
            guest_user = User.objects.get_or_create(username='guest')[0]
            PostViews.objects.create(user=guest_user, blog=instance)

        return Response(serializer.data)


class PostViewsMVS(ModelViewSet):
    queryset = PostViews.objects.all()
    serializer_class = PostViewsSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CommentMVS(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class LikesMVS(ModelViewSet):
    queryset = Likes.objects.all()
    serializer_class = LikesSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

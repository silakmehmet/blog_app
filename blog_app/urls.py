from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import CategoryMVS, BlogMVS, PostViewsMVS, CommentMVS, LikesMVS


router = DefaultRouter()

router.register("categories", CategoryMVS)
router.register("blogs", BlogMVS)
router.register("postviews", PostViewsMVS)
router.register("comments", CommentMVS)
router.register("likes", LikesMVS)

urlpatterns = [
    path("", include(router.urls))
]

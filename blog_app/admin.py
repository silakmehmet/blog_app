from django.contrib import admin

from .models import Category, Blog, PostViews, Comment, Likes

admin.site.register(Category)
admin.site.register(Blog)
admin.site.register(PostViews)
admin.site.register(Comment)
admin.site.register(Likes)

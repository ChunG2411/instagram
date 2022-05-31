from django.contrib import admin
from .models import *

# Register your models here.
class PostModelAdmin(admin.ModelAdmin):
    model = Post
    list_display = ('user', 'created_on', 'updated_on')

class CommentModelAdmin(admin.ModelAdmin):
    model = Comment
    list_display = ('user', 'post','commented_on', 'updated_on')


class LikeModelAdmin(admin.ModelAdmin):
    model = Like
    list_display = ('user', 'post', 'liked_on', 'updated_on')


class FollowModelAdmin(admin.ModelAdmin):
    model = Follow
    list_display = ('user', 'followed', 'followed_on', 'updated_on')


admin.site.register(Post, PostModelAdmin)
admin.site.register(Comment, CommentModelAdmin)
admin.site.register(Like, LikeModelAdmin)
admin.site.register(Follow, FollowModelAdmin)
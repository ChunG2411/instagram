from django.urls import path, include
from .views import *
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('feed/', login_required(views.home), name="feed"),
    path('follow/done', login_required(FollowView.as_view()), name="followed"),
    path('unfollow/done', login_required(UnFollowView.as_view()), name="unfollowed"),
]

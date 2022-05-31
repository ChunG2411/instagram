from django.shortcuts import redirect, render
from django.views import View
from django.contrib.auth import get_user_model
from .models import *

# Create your views here.
User = get_user_model()

def home(request):
    template_name = 'core/feed.html'
    return render(request, template_name)

class FollowView(View):
    def post(self, request, *args, **kwargs):
        followed_user_id = request.POST.get('followed_user_id')
        followed_user_obj = User.objects.get(pk=followed_user_id)

        follow = Follow.objects.create(user=request.user, followed=followed_user_obj)

        return redirect(request.META.get('HTTP_REFERER'))

class UnFollowView(View):
    def post(self, request, *args, **kwargs):
        unfollowed_user_id = request.POST.get('unfollowed_user_id')
        unfollowed_user_obj = User.objects.get(pk=unfollowed_user_id)

        follow = Follow.objects.get(user=request.user, followed=unfollowed_user_obj)
        follow.delete()

        return redirect(request.META.get('HTTP_REFERER'))
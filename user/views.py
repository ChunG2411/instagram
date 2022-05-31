from asyncio import exceptions
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.generic import View
from django.contrib.auth import get_user_model
from core.models import Follow
from .forms import *

# Create your views here.
User = get_user_model()

class Profile(View):
    template_name_anon = 'user/anonymous_profile.html'
    template_name_auth = 'user/authenticated_profile.html'

    def get(self, request, *args, **kwargs):
        username = kwargs.get('username')
        try:
            user = User.objects.get(username=username)
        except Exception as e:
            return HttpResponse('<h1>This page does not exist.</h1>')
        
        if username == request.user.username:
            context = {'user':user}
            return render(request, self.template_name_auth, context)
        else:
            try:
                Follow.objects.get(user=request.user, followed=user)
                is_followed = True
            except Exception as e:
                is_followed = False
            context = {'user':user,'is_followed':is_followed}
            return render(request, self.template_name_anon, context)

class ProfileEdit(View):
    template_name = 'user/profile_edit.html'
    edit_form = UserEditForm

    def get(self, request, *args, **kwargs):
        username = kwargs.get('username')
        if username != request.user.username:
            return HttpResponse('<h1>This page does not exist</h1>')

        form = self.edit_form(instance=request.user)
        context = {'form':form}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = self.edit_form(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile', request.user.username)
        else:
            context = {'form':form}
            return render(request, self.template_name, context)

class Search(View):
    template_name = 'user/all_profiles.html'

    def get(self, request, *args, **kwargs):
        search_term = request.GET.get('query')
        if search_term:
            search_result = User.objects.filter(username__contains=search_term ,full_name__contains=search_term
                                ).exclude(username=request.user.username)
        else:
            search_result = User.objects.none()
        
        context = {'search_result':search_result}
        return render(request, self.template_name, context)

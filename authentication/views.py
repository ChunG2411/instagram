from django.http import HttpResponse
from django.shortcuts import redirect, render
from .forms import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.views import (
                                    PasswordResetView, 
                                    PasswordResetDoneView,
                                    PasswordResetConfirmView,
                                    PasswordResetCompleteView,
                                    PasswordChangeView,
                                    PasswordChangeDoneView,
                                    )
# Create your views here.

User = get_user_model()
def signup(request):
    template_name = 'authentication/signup.html'
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('signin')
    else:
        form = UserForm()
    context = {'form':form}
    return render(request, template_name, context)


def signin(request):
    template_name = 'authentication/signin.html'
    if request.method == "POST":
        email_username = request.POST.get('email_username')
        password = request.POST.get('password')

        try:
            user_obj = User.objects.get(username=email_username)
            email = user_obj.email
        except Exception as e:
            email = email_username
        
        user = authenticate(request, email=email, password=password)
        if user is None:
            messages.success(request, 'Please check your username or password and try again')
            return render(request, template_name)
        else:
            login(request, user)
            return redirect('feed')
    else:
        return render(request, template_name)
    
def signinwithfb(request):
    messages.success(request, 'Not currently able to use this feature, please try another method')
    return redirect('signin')
    
def signout(request):
    logout(request)
    return redirect('signin')


class PRView(PasswordResetView):
    email_template_name = 'authentication/password_reset_email.html'
    template_name = 'authentication/password_reset.html'

class PRDone(PasswordResetDoneView):
    template_name = 'authentication/password_reset_done.html'

class PRConfirm(PasswordResetConfirmView):
    template_name = 'authentication/password_reset_confirm.html'

class PRComplete(PasswordResetCompleteView):
    template_name = 'authentication/password_reset_complete.html'

class PWDChangeView(PasswordChangeView):
    template_name = 'authentication/password_change.html'

class PWDChangeDoneView(PasswordChangeDoneView):
    template_name = 'authentication/password_change_done.html'
    

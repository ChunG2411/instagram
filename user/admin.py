from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *
from authentication.forms import *

# Register your models here.
class CustomUserAdmin(UserAdmin):
    add_form = UserForm
    form = CustomUserChangeForm
    model = User
    add_fieldsets = (
        ('Personal Details', {'fields': ('email', 'full_name', 'username', 'picture', 'password1', 'password2')}),
        ('Optional', {'fields': ('biography', 'website')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
        )
    fieldsets = (
        ('Personal Details', {'fields': ('email', 'full_name', 'username', 'picture')}),
        ('Optional', {'fields': ('biography', 'website')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
        )

admin.site.register(User, CustomUserAdmin)
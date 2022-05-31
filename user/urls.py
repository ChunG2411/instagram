from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('profile/<str:username>/', login_required(Profile.as_view()), name='profile'),
    path('profile/<str:username>/edit/', login_required(ProfileEdit.as_view()), name='profile_edit'),
    path('search/', login_required(Search.as_view()), name="search")
]

if settings.DEBUG:
     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
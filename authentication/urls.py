from django.urls import path, include
from .views import *

urlpatterns = [
    path('', signin, name ="signin"),
    path('signup/', signup, name="signup"),
    path('signout/', signout, name="signout"),
    path('signin_fb/', signinwithfb, name="signinwithfb"),

    path('password/reset/', PRView.as_view(), name='password_reset'),
    path('password/reset/done/',  PRDone.as_view() ,name='password_reset_done'),
    path('password/reset/confirm/<uidb64>/<token>', PRConfirm.as_view() , name='password_reset_confirm'),
    path('password/reset/complete/', PRComplete.as_view() , name='password_reset_complete'),
    path('password/change', PWDChangeView.as_view() , name='password_change'),
    path('password/change/done', PWDChangeDoneView.as_view() , name='password_change_done'),
]

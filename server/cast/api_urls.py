__author__ = "RituRaj"

from django.conf.urls import url

import code_analyze.views
import cast_auth.views

urlpatterns = [
    url('code_analyze',
        code_analyze.views.CodeAnalyzeApi.as_view(),
        name="code_analyze"),

    # Login
    url('user/login/',
        cast_auth.views.UserAuthLoginView.as_view(), name="login"),

    # Register a new user
    url('user/register',
        cast_auth.views.UserRegisterationView.as_view(), name="register_user"),

   
]

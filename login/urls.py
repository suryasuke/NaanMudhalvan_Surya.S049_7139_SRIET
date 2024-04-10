from django.urls import path
from . import views as login_views  # Import views from the same app


urlpatterns = [
    path('login/', login_views.login, name='login'),
    path('login_view/', login_views.login_view, name='login_view'),
    path('signup/', login_views.signup_view, name='signup'),
    path('forgot_password/', login_views.forgot_password, name='forgot_password'),
    path('studenthome/', login_views.student_home, name='studenthome'),
]

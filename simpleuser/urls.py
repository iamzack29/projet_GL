from django.urls import include, re_path,path
from . import views


app_name = 'simpleuser'
urlpatterns = [
    path("", views.home , name="home"),
    path("signup/", views.signup, name="signup"),
    path("logout/", views.logout_view , name="logout"),
    path("signin/", views.login_view, name="signin"),
    path("profile/", views.profile_view, name="profile"),

]

from django.urls import include, re_path,path
from . import views


app_name = 'announecements'
urlpatterns = [
    path("view/<int:annonce_id>", views.s_annonce , name="view"),]
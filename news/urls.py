from django.urls import path, include, re_path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('publish', views.publish, name="publish"),
    path('email', views.notify_admin, name="notify_admin"),
    re_path(r'^view/(?P<post_id>[a-z0-9]+)/$', views.view_post, name="view_post"),
]
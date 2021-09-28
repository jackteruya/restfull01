from django.conf.urls import url
from django.urls import path, re_path
from toys import views

urlpatterns = [
    re_path(r'toys/$', views.toy_list),
    re_path(r'toys/(?P<pk>[0-9]+)$', views.toy_detail),
]

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^logout/$', views.logout_view, name='logout_view'),
    url(r'^post_list/$', views.post_new, name='post_new'),
    url(r'^post_new$', views.post_new, name='post_new'),  
    url(r'^post_edit/(?P<pk>[0-9]+)/$', views.post_edit, name='post_edit'),
    url(r'^post_del/(?P<pk>[0-9]+)/$', views.post_del, name='post_del'),
]
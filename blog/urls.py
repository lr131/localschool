from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^logout/$', views.logout_view, name='logout_view'),
    url(r'^post_list/$', views.post_list, name='post_list'),
    url(r'^rasp_list/$', views.rasp_list, name='rasp_list'),
    url(r'^plan_page/$', views.plan_page, name='plan_page'),
    url(r'^rasp_zv/$', views.rasp_zv, name='rasp_zv'),
    url(r'^rasp_change/$', views.rasp_change, name='rasp_change'),
    url(r'^post_new$', views.post_new, name='post_new'),  
    url(r'^post_edit/(?P<pk>[0-9]+)/$', views.post_edit, name='post_edit'),
    url(r'^post_del/(?P<pk>[0-9]+)/$', views.post_del, name='post_del'),
]
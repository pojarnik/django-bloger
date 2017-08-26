from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name = 'post_list'),
    url(r'^new/$', views.post_new, name = 'post_new'),
    url(r'^edit/(?P<key>[0-9]+)/(?P<key2>[0-9]+)/$', views.post_edit, name = 'post_edit'),
]
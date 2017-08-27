from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.who_is_on_post, name = 'who_is_on_post'),
]
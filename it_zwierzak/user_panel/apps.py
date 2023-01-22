from django.conf.urls import patterns, url
from homepage import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^register_profile/$', views.register_profile, name='register_profile'),
        url(r'^(?P<username>\w+)/$', views.profile_page, name='user_profile'),
        )
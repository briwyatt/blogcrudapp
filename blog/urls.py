from django.conf.urls import patterns, url

from blog import views

urlpatterns = patterns('',
  url(r'^$', views.BlogList.as_view(), name='blog_list'),
  url(r'^new$', views.BlogCreate.as_view(), name='blog_new'),
  url(r'^edit/(?P<pk>\d+)$', views.BlogUpdate.as_view(), name='blog_edit'),
  url(r'^delete/(?P<pk>\d+)$', views.BlogDelete.as_view(), name='blog_delete'),
)
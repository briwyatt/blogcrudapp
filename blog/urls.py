from django.conf.urls import patterns, url

from blog import views

urlpatterns = patterns('',
  url(r'^$', views.BlogList.as_view(), name='list'),
  url(r'^new$', views.BlogCreate.as_view(), name='new'),
  url(r'^edit/(?P<pk>\d+)$', views.BlogUpdate.as_view(), name='edit'),
  url(r'^delete/(?P<pk>\d+)$', views.BlogDelete.as_view(), name='delete'),
)
from django.conf.urls import patterns, include, url
from home import views

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    #url(r'^survey/(?P<sid>\d+)/$', views.displaySurvey),
    #url(r'^createsurvey/', views.createSurvey)
    url(r'^home/', views.homepage),
    url(r'^survey/(?P<sid>\d+)/$', views.displaySurvey),
    url(r'^survey/(?P<sid>\d+)/vote/', views.handleVote),
    url(r'^survey/(?P<sid>\d+)/comment/', views.handleComment),
    url(r'^browse/', views.browse),
    url(r'^new/$', views.createSurvey),
    url(r'^new/create/', views.handleForm)
)


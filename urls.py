from django.conf.urls import patterns, include, url
import views

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^survey/(?P<sid>\d+)/$', views.displaySurvey),
    url(r'^createsurvey/', views.createSurvey)
)

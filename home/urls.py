from django.conf.urls import patterns, include, url
import views

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^home/', views.homepage),
    url(r'^survey/(?P<sid>\d+)/$', views.displaySurvey),
    url(r'^browse/', views.browse),
    url(r'^new/$', views.createSurvey),
    url(r'^new/create/', views.handleForm)
)

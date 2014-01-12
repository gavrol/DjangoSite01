from django.conf.urls import patterns, include, url
import Charnwood.views
import Charnwood.settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    #url(r'^$', Charnwood.views.CharnwoodInfo), #'Charnwood.views.home', name='home'),
    #url(r'^index/$',Charnwood.views.CharnwoodInfo),
    url(r'^Charnwood/$',Charnwood.views.CharnwoodInfo),
    url(r'^RBCSgrievances/$',Charnwood.views.RBCSgrievances),
    url(r'^SpecialGeneralMeeting/$',Charnwood.views.SpecialGeneralMeeting),
    url(r'^contact/$',Charnwood.views.contact),
    #url(r'^RBCSgrievances/$',Charnwood.views.Charnwood,{'template_name':"RBCSgrievances"}),	
    #url(r'^admin/', include(admin.site.urls)),
)

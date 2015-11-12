from django.conf.urls import patterns, url
from books.views import *
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    #('^hello/$',hello) ,
    url(r'^time/$',time),
    url(r'^test/$',test),
    url(r'search-form/$',search_form),
    url(r'^search/$',search),
    url(r'^delete/$',Delete),
    url(r'^add/$',add),
    url(r'^addbook/$',addbook),
    url(r'^up/$',up),
    url(r'^update/$',update),
    url(r'^check/$',check),


    url(r'^admin/', admin.site.urls),
    
)

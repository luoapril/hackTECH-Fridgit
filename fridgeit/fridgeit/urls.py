from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
<<<<<<< Updated upstream
    url(r'^$', 'fridgeit.views.home', name='home'),
    url(r'^login/$', 'django.contrib.auth.views.login', name="login"),
    url(r'^logout/$', 'fridgeit.views.logout_page'),
     url(r'^$', 'fridgeit.views.index', name='index'),
=======
     url(r'^$', 'fridgeit.views.home', name='home'),
     url(r'^index', 'fridgeit.views.index', name='index'),
     url(r'^signup', 'fridgeit.views.signup', name='signup'),
>>>>>>> Stashed changes
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)

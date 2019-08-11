from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url('^$',views.index,name = 'index'),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^profile$', views.profile, name='profile'),
    url(r'^home$', views.home, name='home'),
    url(r'^view$', views.view, name='view'),
    url(r'^new/neighbourhood$', views.new_hood, name='new-hood'),
    url(r'^new/profile$', views.new_profile, name='new-profile')
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
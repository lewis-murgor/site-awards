from django.urls import re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    re_path('^$',views.index,name='index'),
    re_path(r'^accounts/profile', views.profile, name='profile'),
    re_path(r'^project/(\d+)',views.project,name ='project'),
    re_path(r'^post/project$', views.post_project, name='post-project'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
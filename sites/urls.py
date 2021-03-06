from django.urls import re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    re_path('^$',views.index,name='index'),
    re_path(r'^search/', views.search_results, name='search_results'),
    re_path(r'^accounts/profile', views.profile, name='profile'),
    re_path(r'^update/profile$', views.update_profile, name='update-profile'),
    re_path(r'^project/(\d+)',views.project,name ='project'),
    re_path(r'^post/project$', views.post_project, name='post-project'),
    re_path(r'^api/profile/$', views.ProfileList.as_view()),
    re_path(r'^api/project/$', views.ProjectList.as_view()),
    re_path(r'api/profile/profile-id/(?P<pk>[0-9]+)/$',views.ProfileDescription.as_view()),
    re_path(r'api/project/project-id/(?P<pk>[0-9]+)/$',views.ProjectDescription.as_view())
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.urls.conf import path,re_path

urlpatterns=[
    path('',views.home,name = 'home'),
    path('profile/',views.profile,name='profile'),
    path('search/',views.search,name='search'),
    path('project/<int:project_id>',views.detail,name='project.detail'),
    path('details/<int:project_id>',views.detail,name='details'),
    path('post/',views.post_project,name='post'),
    path('update/',views.update_profile,name='update'),
    re_path(r'^users/(?P<pk>\d+)$',views.users_profile,name='users_profile'),
    re_path(r'^delete/(?P<project_id>\d+)$',views.delete,name='delete'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
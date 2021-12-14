from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.urls.conf import path,re_path
from django.contrib.auth import views as auth_views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns=[
    path('',views.home,name = 'home'),
    path('profile/',views.profile,name='profile'),
    path('search/',views.search,name='search'),
    path('project/<int:project_id>',views.detail,name='project.detail'),
    path('details/<int:project_id>',views.detail,name='details'),
    path('post/',views.post_project,name='post'),
    path('update/',views.update_profile,name='update'),
    path('accounts/register/',views.register,name='register'),
    path('',auth_views.LoginView.as_view(template_name = 'registration/login.html'),name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name = 'registration/logout.html'),name='logout'),
    path(r'^users/(?P<pk>\d+)$',views.users_profile,name='users_profile'),
    path(r'^delete/(?P<project_id>\d+)$',views.delete,name='delete'),
    path('api/projects/',views.ProjectList.as_view()),
    path('api/profiles/',views.ProfileList.as_view()),
    path('api_token/', obtain_auth_token),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
from django.urls import path, include
from django.conf.urls import url
from django.views.generic.base import TemplateView
from django.contrib.auth.decorators import login_required
from . import views


urlpatterns = [
    path('',
         TemplateView.as_view(template_name='home.html'), name='home'),
    path('<int:user_id>', login_required(views.profile), name='profile'),
    # url(
    #     r'users/(?P<user_id>\w+)$',
    #     views.UserProfileView.as_view(),
    #     name='user_profile',
    # ),
    # path('user<int:user_id>', views.UserProfileView.as_view(),
    #      name='user_profile'),
    path('', include('django.contrib.auth.urls')),
    path('signup', views.signup, name='signup'),


]

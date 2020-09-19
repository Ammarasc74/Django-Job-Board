from django.urls import path

from . import views
from . import api



app_name='accounts'


urlpatterns = [
    path('signup',views.signup, name ='signup'),
    path('profile',views.profile, name ='profile'),
    path('profile/edit',views.profile_edit, name ='profile_edit'),


    # api

    path('accounts/api/register', api.User_Api.as_view(),name='User'),
    path('accounts/api/users', api.All_Users_Api.as_view(),name='User'),
    path('accounts/api/users/<int:id>', api.User_Detail_Api.as_view(),name='User detail'),
    # path('accounts/api/<int:id>', api.User_login_Api.as_view(),name='User login'),
    


]
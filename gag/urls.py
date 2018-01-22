from . import views
from django.urls import path
from django.conf.urls import url
from django.contrib.auth import views as auth_views

app_name = 'gag'

urlpatterns = [
    path('',views.index, name='index'),
    path('posts/<int:pk>/', views.DetailsView.as_view(), name='details'),
    #path('like/<int:id/', views.like, name='like'),
    #url(r'like/(?P<int:id>\d+)/$', views.like, name='like')
    path('like/<id>/', views.like, name='like'),
    path('login/', auth_views.login, name='login'),
    path('logout/', views.logout_view, name='logout'),
    #url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name='logout'),
    path('accounts/profile/', views.profile, name='profile'),
    path('signup/', views.signup, name='signup'),
]
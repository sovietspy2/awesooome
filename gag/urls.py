from . import views
from django.urls import path
from django.conf.urls import url

app_name = 'gag'

urlpatterns = [
    path('',views.index, name='index'),
    path('posts/<int:pk>/', views.DetailsView.as_view(), name='details'),
    #path('like/<int:id/', views.like, name='like'),
    #url(r'like/(?P<int:id>\d+)/$', views.like, name='like')
    path('like/<id>/', views.like, name='like')
]
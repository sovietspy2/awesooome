from . import views
from django.urls import path

app_name = 'gag'

urlpatterns = [
    path('',views.index, name='index'),
    path('posts/<int:pk>/', views.DetailsView.as_view(), name='details'),
]
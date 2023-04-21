from django.urls import path
from . import views

urlpatterns = [
    path('jobs/', views.getAllJobs, name='jobs'),
    path('job/new', views.newJob, name='new_job'),
    path('job/<str:pk>/', views.getJob, name='job'),
    path('job/<str:pk>/update', views.updateJob, name='update_job'),
    path('job/<str:pk>/delete', views.deleteJob, name='delete_job'),
    path('stats/<str:topic>/', views.getTopicStats, name='get_topic_stats')


               ]
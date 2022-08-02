from . import views
from django.urls import path
from .feeds import LatestJobPostsFeed

urlpatterns = [
    path('', views.JobList.as_view(), name='jobs'),
    path('/feeds', LatestJobPostsFeed(), name='latest_job_posts_feed'),
    path('/latest_job', views.LatestJob.as_view(), name='latest_job'),
    path('/admit_card', views.AdmitCard.as_view(), name='admit_card'),
    path('/result', views.Result.as_view(), name='result'),
    path('/<slug:slug>/', views.job_detail, name='job_detail'),
]

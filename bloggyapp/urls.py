from . import views
from django.urls import path
from .views import SearchResultsView
from .views import emailView
from django.contrib import admin
from .feed import LatestPostsFeed





urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('feed/', LatestPostsFeed(), name='latest_posts_feed'),
    path('admin/', admin.site.urls),
    path('search/', SearchResultsView.as_view(), name='search_results'),
    path('about/', views.about, name="about"),
    path('gate/', views.gate, name="gate"),
    path('science/', views.science, name="science"),
    path('sciencesyllabus/', views.sciencesyllabus, name="sciencesyllabus"),
    path('chemistry/', views.chemistry, name="chemistry"),
    path('upsc/', views.upsc, name="upsc"),
    path('library/', views.library, name="library"),
    path('tutorial/', views.tutorial, name="tutorial"),
    path('email/', views.emailView, name="email"),
    path('disclaimer/', views.disclaimer, name="disclaimer"),
    path('privacy/', views.privacy, name="privacy"),
    path('angularblog/',views.AngularList.as_view(), name="angularblog"),
    path('reactblog/',views.ReactList.as_view(), name="reactblog"),
    path('djangoblog/',views.DjangoList.as_view(), name="djangoblog"),
    path('nodeblog/',views.NodeList.as_view(), name="nodeblog"),
    path('programblog/',views.ProgramBlog.as_view(), name="programblog"),
    path('pythonblog/',views.PythonBlog.as_view(), name="pythonblog"),
    path('javablog/',views.JavaBlog.as_view(), name="javablog"),
    path('datascience/',views.DataScience.as_view(), name="datascience"),
    path('basicprogram/',views.BasicProgram.as_view(), name="basicprogram"),
    path('listofprogram/',views.ListofProgram.as_view(), name="listofprogram"),
    path('physicslecture/',views.PhysicsLecture.as_view(), name="physicslecture"),
    path('new/', views.new, name='new'),
    path('confirm/', views.confirm, name='confirm'),
    path('delete/', views.delete, name='delete'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),


]

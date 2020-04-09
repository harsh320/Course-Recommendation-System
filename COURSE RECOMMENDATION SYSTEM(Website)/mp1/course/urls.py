from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include
from django.views.generic import RedirectView
from . import views
urlpatterns = [

    path('',views.index,name='index'),
    path('register/',views.register_view,name='register'),
    path('login/',views.login_view,name='login'),
    path('logout/',views.logout_view,name='logout'),
    path('SearchCourses/',views.search_course, name='search_course'),
    path('SearchCourses/<slug:query>/',views.search_course,name = 'search_course'),
    path('Courses/',views.course, name='course'),
    path('AboutProject/',views.about_project,name='about_project'),
    path('AboutUs/',views.about_us,name='about_us'),
    path('Courses/<int:pk>/',views.all_courses,name='all_courses'),
    path('Courses/<int:pk>/<int:branchid>',views.online_courses,name='online_courses'),
    path('Courses/<int:pk>/<int:branchid>/<int:name>',views.course_details,name='cd'),
    path('forum/',views.forum,name='forum'),
    path('add-question',views.add_question,name='add_question'),
    path('tag/<slug:tag_name>/',views.tags_view,name='tag_view'),
    path('thread/<slug:thread_id>/',views.thread_view,name="thread_view"),


]
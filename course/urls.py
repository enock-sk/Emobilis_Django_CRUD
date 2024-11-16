from django.urls import path

from . import views
app_name="course"
urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('courses/',views.courses,name='courses'),
    path('course_details/',views.course_details,name='course_details'),
    path('events/',views.events,name='events'),
    path('pricing/',views.pricing,name='pricing'),
    path('startpage/',views.startpage,name='startpage'),
    path('trainers/',views.trainers,name='trainers'),

]
from django.urls import path 
from . import views
urlpatterns = [
    path('',views.Home.as_view(),name='home'),
    path('facility/',views.Blog.as_view(),name='blog'),
    path('about/',views.About.as_view(),name='about'),
    path('result/',views.Result_view.as_view(),name='result'),
    path('service/',views.Service.as_view(),name='service'),
    path('contact/',views.Contact.as_view(),name='contact'),
    path('student-update/<uuid:pk>/',views.StudentRegisterUpdate.as_view(),name='update'),
    path('login/',views.Login.as_view(),name='login'),
    path('student/<slug:slug>/',views.StudentProfile.as_view(),name='student'),
    path('logout/',views.Logout,name='logout'),
]
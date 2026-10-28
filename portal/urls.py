"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from portal import views
from .models import StudentProfile, Gallery

urlpatterns = [
    path("", views.index, name="home"),
    path("home", views.index, name="home"),
    path("about_institute", views.about_institute, name="about_institute"),
    path("facilities", views.facilities, name="facilities"),
    path("admission_enquiry", views.admission_enquiry, name="admission_enquiry"),
    path("contect", views.contect, name="contect"),
    path("courses_mmhapu", views.courses_mmhapu, name="courses_mmhapu"),
    path("courses_ncpul", views.courses_ncpul, name="courses_ncpul"),
    path("from_mmhapu", views.from_mmhapu, name="from_mmhapu"),
    path("from_ncpul", views.from_ncpul, name="from_ncpul"),
    path("gallery", views.gallery, name="gallery"),
    path("news", views.news, name="news"),
    path("university_fee", views.university_fee, name="university_fee"),
    path("our_organization", views.our_organization, name="our_organization"),
    path("our_mission_vision", views.our_mission_vision, name="our_mission_vision"),
    path("our_motto", views.our_motto, name="our_motto"),
    path("affiliation", views.affiliation, name="affiliation"),
    path("location", views.location, name="location"),
    path("admission_form", views.form_data_admission, name="admission_form"),
    path("tiitpanel", admin.site.urls, name="admin"),
    path("faculty_portal", views.faculty_portal, name="faculty_portal"),
    path("student_portal", views.student_portal, name="student_portal"),
    path("faculty_dashboard", views.faculty_dashboard, name="faculty_dashboard"),
    path("student_dashboard", views.student_dashboard, name="student_dashboard"),
    path("logout", views.user_logout, name="logout"),
    path('results/', views.exam_results, name='exam_results'),
    
    path("form_data_admission", views.form_data_admission, name="form_data_admission"),
    path("form_data_admission_enquiry", views.form_data_admission_enquiry, name="form_data_admission_enquiry")
]




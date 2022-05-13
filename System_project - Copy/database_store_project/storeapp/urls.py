from django.urls import path

from . import views

urlpatterns = [path("", views.homepage, name="homepage_user"),
               path("about-us/", views.about_us, name="information"),
               path("Patient/", views.Patient, name="Patient"),
               path("Details/", views.details, name="details"),
               # path("Admin_page/", views.Admin_view, name="admin_view"),
               ]

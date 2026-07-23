from django.urls import path
from . import views

urlpatterns = [

    path("", views.home, name="home"),

    path("register/", views.register, name="register"),

    path("submit-paper/", views.submit_paper, name="submit_paper"),

    path("contact/", views.contact, name="contact"),

    path("dashboard/", views.dashboard, name="dashboard"),

    path("broadcast/", views.broadcast, name="broadcast"),

    path("payment/<int:pk>/", views.payment, name="payment"),

    path("dashboard/registrations/", views.registration_list, name="registration_list"),

    path("dashboard/papers/", views.paper_list, name="paper_list"),

    path("dashboard/speakers/", views.speaker_list, name="speaker_list"),

    path("dashboard/committee/", views.committee_list, name="committee_list"),

    path("dashboard/gallery/", views.gallery_list, name="gallery_list"),

    path("dashboard/schedule/", views.schedule_list, name="schedule_list"),

    path("dashboard/venue/", views.venue_list, name="venue_list"),

    path("dashboard/announcements/", views.announcement_list, name="announcement_list"),
 
    path("dashboard/settings/", views.website_settings, name="website_settings"),


]
from django.contrib import admin
from .broadcast import send_email_to_all, send_whatsapp_to_all
from .models import (
    ConferenceSettings,
    VenueLocation,
    Registration,
    ConferenceTrack,
    PaperSubmission,
    Speaker,
    Announcement,
    Schedule,
    Gallery,
    ContactMessage,
    BroadcastMessage
)
admin.site.site_header = "Conference Management System"

admin.site.site_title = "Conference Admin"

admin.site.index_title = "Administration Dashboard"

def send_selected_broadcasts(modeladmin, request, queryset):

    for obj in queryset:

        try:
            if obj.send_email:
                send_email_to_all(obj.subject, obj.message)

            if obj.send_whatsapp:
                send_whatsapp_to_all(obj.message)

            obj.status = "Sent"

        except Exception:
            obj.status = "Failed"

        obj.save()

    modeladmin.message_user(
        request,
        "Selected broadcasts processed successfully."
    )

send_selected_broadcasts.short_description = "Send selected broadcasts"

@admin.register(BroadcastMessage)
class BroadcastMessageAdmin(admin.ModelAdmin):
    actions = [send_selected_broadcasts]

    list_display = (
        "subject",
        "status",
        "send_email",
        "send_whatsapp",
        "created_at",
    )

    list_filter = (
        "status",
        "send_email",
        "send_whatsapp",
    )

    ordering = ("-created_at",)

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)

        self.message_user(
            request,
            "Broadcast saved successfully. Ready to send."
        )
@admin.register(PaperSubmission)
class PaperSubmissionAdmin(admin.ModelAdmin):

    list_display = (
        "paper_title",
        "author_name",
        "email",
        "status",
    )

    search_fields = (
        "paper_title",
        "author_name",
        "email",
    )

    list_filter = (
        "status",
    )
    list_per_page =20

    ordering = (
        "-id",
    )
@admin.register(Speaker)
class SpeakerAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "designation",
        "organization",
    )

    search_fields = (
        "name",
        "organization",
    )
    
    list_per_page = 20

    ordering = (
        "name",
    )
@admin.register(Announcement)
class AnnouncementAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "created_at",
    )

    ordering = (
        "-created_at",
    )
@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "email",
        "subject",
        "created_at",
    )

    search_fields = (
        "name",
        "email",
        "subject",
    )
    list_per_page = 20

    ordering = (
        "-created_at",
    )
@admin.register(ConferenceSettings)
class ConferenceSettingsAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "venue",
        "start_date",
        "end_date",
    )
@admin.register(VenueLocation)
class VenueLocationAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "google_map_link",
    )

    search_fields = (
        "name",
    )
@admin.register(ConferenceTrack)
class ConferenceTrackAdmin(admin.ModelAdmin):

    list_display = (
        "name",
    )

    search_fields = (
        "name",
    )
@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "uploaded_at",
    )

    ordering = (
        "-uploaded_at",
    )
@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):

    list_display = (
        "time",
        "event",
    )

    ordering = (
        "time",
    )
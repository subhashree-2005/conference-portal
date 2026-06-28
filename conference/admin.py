from django.contrib import admin

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

admin.site.register(ConferenceSettings)
admin.site.register(VenueLocation)
admin.site.register(Registration)
admin.site.register(ConferenceTrack)
admin.site.register(PaperSubmission)
admin.site.register(Speaker)
admin.site.register(Announcement)
admin.site.register(Schedule)
admin.site.register(Gallery)
admin.site.register(ContactMessage)
admin.site.register(BroadcastMessage)
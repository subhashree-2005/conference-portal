from django.contrib import admin
from django.utils.html import format_html
from django.utils import timezone

from .models import (
    WebsiteSettings,
    AboutConference,
    ConferenceTrack,
    ImportantDate,
    Speaker,
    CommitteeMember,
    Gallery,
    VenueLocation,
    Schedule,
    Registration,
    RegistrationFee,
    PaymentSettings,
    PaperSubmission,
    Announcement,
    ContactMessage,
    BroadcastMessage,
    Statistics,
)

# =====================================================
# WEBSITE SETTINGS
# =====================================================

@admin.register(WebsiteSettings)
class WebsiteSettingsAdmin(admin.ModelAdmin):

    list_display = (
        "conference_name",
        "short_name",
        "organization",
        "conference_date",
        "venue",
        "email",
    )

    search_fields = (
        "conference_name",
        "organization",
        "short_name",
        "email",
    )

    fieldsets = (

        ("Conference Details", {
            "fields": (
                "conference_name",
                "short_name",
                "organization",
                "department",
            )
        }),

        ("Hero Section", {
            "fields": (
                "hero_heading",
                "hero_subtitle",
                "conference_date",
                "venue",
            )
        }),

        ("Contact", {
            "fields": (
                "email",
                "phone",
                "address",
                "website",
            )
        }),

        ("Social Links", {
            "fields": (
                "facebook",
                "linkedin",
                "twitter",
                "instagram",
            )
        }),

        ("Branding", {
            "fields": (
                "primary_color",
                "secondary_color",
                "conference_logo",
                "organization_logo",
                "hero_image",
                "favicon",
            )
        }),

        ("Footer", {
            "fields": (
                "copyright",
            )
        }),

    )


# =====================================================
# ABOUT CONFERENCE
# =====================================================

@admin.register(AboutConference)
class AboutConferenceAdmin(admin.ModelAdmin):

    list_display = (
        "title",
    )

    search_fields = (
        "title",
    )

    fieldsets = (

        ("About Conference", {
            "fields": (
                "title",
                "description",
                "vision",
                "mission",
                "image",
            )
        }),

    )


# =====================================================
# TRACKS
# =====================================================

@admin.register(ConferenceTrack)
class ConferenceTrackAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "icon",
    )

    search_fields = (
        "name",
        "description",
    )

    ordering = (
        "name",
    )

    list_per_page = 20


# =====================================================
# IMPORTANT DATES
# =====================================================

@admin.register(ImportantDate)
class ImportantDateAdmin(admin.ModelAdmin):

    list_display = (
        "event",
        "date",
        "description",
    )

    search_fields = (
        "event",
    )

    ordering = (
        "date",
    )

    list_per_page = 20


# =====================================================
# SPEAKERS
# =====================================================

@admin.register(Speaker)
class SpeakerAdmin(admin.ModelAdmin):

    list_display = (
        "photo_preview",
        "name",
        "designation",
        "organization",
    )

    search_fields = (
        "name",
        "designation",
        "organization",
    )

    ordering = (
        "name",
    )

    list_per_page = 20

    fieldsets = (

        ("Speaker Details", {
            "fields": (
                "name",
                "designation",
                "organization",
                "biography",
            )
        }),

        ("Social", {
            "fields": (
                "linkedin",
            )
        }),

        ("Photo", {
            "fields": (
                "photo",
            )
        }),

    )

    def photo_preview(self, obj):

        if obj.photo:

            return format_html(
                '<img src="{}" width="60" height="60" style="border-radius:50%;object-fit:cover;">',
                obj.photo.url,
            )

        return "-"

    photo_preview.short_description = "Photo"


# =====================================================
# COMMITTEE
# =====================================================

@admin.register(CommitteeMember)
class CommitteeMemberAdmin(admin.ModelAdmin):

    list_display = (
        "photo_preview",
        "name",
        "designation",
        "organization",
    )

    search_fields = (
        "name",
        "designation",
        "organization",
    )

    ordering = (
        "name",
    )

    list_per_page = 20

    fieldsets = (

        ("Committee Member", {
            "fields": (
                "name",
                "designation",
                "organization",
            )
        }),

        ("Photo", {
            "fields": (
                "photo",
            )
        }),

    )

    def photo_preview(self, obj):

        if obj.photo:

            return format_html(
                '<img src="{}" width="60" height="60" style="border-radius:50%;object-fit:cover;">',
                obj.photo.url,
            )

        return "-"

    photo_preview.short_description = "Photo"
# =====================================================
# GALLERY
# =====================================================

@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):

    list_display = (
        "preview",
        "title",
        "uploaded_at",
    )

    search_fields = (
        "title",
    )

    readonly_fields = (
        "uploaded_at",
    )

    ordering = (
        "-uploaded_at",
    )

    list_per_page = 20

    def preview(self, obj):

        if obj.image:

            return format_html(
                '<img src="{}" width="120" style="border-radius:8px;">',
                obj.image.url,
            )

        return "-"

    preview.short_description = "Preview"


# =====================================================
# VENUE
# =====================================================

@admin.register(VenueLocation)
class VenueLocationAdmin(admin.ModelAdmin):

    list_display = (
        "preview",
        "name",
        "address",
    )

    search_fields = (
        "name",
        "address",
    )

    list_per_page = 20

    def preview(self, obj):

        if obj.image:

            return format_html(
                '<img src="{}" width="120" style="border-radius:8px;">',
                obj.image.url,
            )

        return "-"

    preview.short_description = "Image"


# =====================================================
# SCHEDULE
# =====================================================

@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):

    list_display = (
        "day",
        "time",
        "event",
        "speaker",
        "venue",
    )

    search_fields = (
        "event",
        "speaker",
        "venue",
    )

    ordering = (
        "day",
        "time",
    )

    list_per_page = 30


# =====================================================
# REGISTRATION
# =====================================================

@admin.register(Registration)
class RegistrationAdmin(admin.ModelAdmin):

    list_display = (
        "full_name",
        "email",
        "organization",
        "country",
        "category",
        "registration_fee",
        "payment_badge",
        "receipt",
        "registered_at",
    )

    list_filter = (
        "category",
        "payment_status",
        "payment_verified",
        "country",
        "registered_at",
    )

    search_fields = (
        "full_name",
        "email",
        "organization",
        "phone",
        "transaction_id",
    )

    readonly_fields = (
        "registered_at",
        "verified_date",
    )

    ordering = (
        "-registered_at",
    )

    date_hierarchy = "registered_at"

    list_per_page = 20

    actions = (
        "approve_payment",
        "reject_payment",
        "mark_pending",
    )

    fieldsets = (

        ("Participant Details", {
            "fields": (
                "full_name",
                "email",
                "phone",
                "gender",
                "organization",
                "designation",
                "country",
                "city",
            )
        }),

        ("Conference Details", {
            "fields": (
                "category",
                "registration_fee",
            )
        }),

        ("Payment", {
            "fields": (
                "payment_status",
                "payment_verified",
                "transaction_id",
                "payment_receipt",
            )
        }),

        ("Verification", {
            "fields": (
                "verified_by",
                "verified_date",
                "remarks",
            )
        }),

        ("System", {
            "fields": (
                "registered_at",
            )
        }),

    )

    # ==========================================
    # PAYMENT BADGE
    # ==========================================

    def payment_badge(self, obj):

        colors = {
            "Paid": "#198754",
            "Pending": "#ffc107",
            "Rejected": "#dc3545",
        }

        return format_html(
            '<span style="background:{};color:white;padding:6px 15px;border-radius:25px;font-weight:bold;">{}</span>',
            colors.get(obj.payment_status, "#6c757d"),
            obj.payment_status,
        )

    payment_badge.short_description = "Payment"

    # ==========================================
    # RECEIPT
    # ==========================================

    def receipt(self, obj):

        if obj.payment_receipt:

            return format_html(
                '<a href="{}" target="_blank" class="button">View Receipt</a>',
                obj.payment_receipt.url,
            )

        return "-"

    receipt.short_description = "Receipt"

    # ==========================================
    # APPROVE
    # ==========================================

    @admin.action(description="Approve Selected Payments")
    def approve_payment(self, request, queryset):

        for registration in queryset:

            registration.payment_status = "Paid"
            registration.payment_verified = True
            registration.verified_by = request.user.username
            registration.verified_date = timezone.now()

            registration.save()

    # ==========================================
    # REJECT
    # ==========================================

    @admin.action(description="Reject Selected Payments")
    def reject_payment(self, request, queryset):

        for registration in queryset:

            registration.payment_status = "Rejected"
            registration.payment_verified = False
            registration.verified_by = request.user.username
            registration.verified_date = timezone.now()

            registration.save()

    # ==========================================
    # MARK PENDING
    # ==========================================

    @admin.action(description="Mark Selected Pending")
    def mark_pending(self, request, queryset):

        for registration in queryset:

            registration.payment_status = "Pending"
            registration.payment_verified = False
            registration.verified_by = ""
            registration.verified_date = None

            registration.save()
# =====================================================
# REGISTRATION FEES
# =====================================================

@admin.register(RegistrationFee)
class RegistrationFeeAdmin(admin.ModelAdmin):

    list_display = (
        "category",
        "indian_fee",
        "foreign_fee",
        "currency",
        "active",
        "display_order",
    )

    list_editable = (
        "indian_fee",
        "foreign_fee",
        "active",
        "display_order",
    )

    list_filter = (
        "active",
    )

    search_fields = (
        "category",
    )

    ordering = (
        "display_order",
    )

    list_per_page = 20


# =====================================================
# PAYMENT SETTINGS
# =====================================================

@admin.register(PaymentSettings)
class PaymentSettingsAdmin(admin.ModelAdmin):

    list_display = (
        "upi_id",
        "bank_name",
        "support_email",
        "registration_deadline",
    )

    fieldsets = (

        ("Conference Deadlines", {
            "fields": (
                "registration_deadline",
                "early_bird_deadline",
                "camera_ready_deadline",
            )
        }),

        ("UPI Payment", {
            "fields": (
                "upi_id",
                "qr_code",
            )
        }),

        ("Bank Details", {
            "fields": (
                "account_name",
                "bank_name",
                "account_number",
                "ifsc_code",
                "swift_code",
            )
        }),

        ("Support", {
            "fields": (
                "support_email",
                "payment_note",
            )
        }),

    )


# =====================================================
# PAPER SUBMISSION
# =====================================================

@admin.register(PaperSubmission)
class PaperSubmissionAdmin(admin.ModelAdmin):

    list_display = (
        "paper_title",
        "author_name",
        "email",
        "status_badge",
        "submitted_at",
    )

    list_filter = (
        "status",
    )

    search_fields = (
        "paper_title",
        "author_name",
        "email",
        "keywords",
    )

    ordering = (
        "-submitted_at",
    )

    readonly_fields = (
        "submitted_at",
    )

    date_hierarchy = "submitted_at"

    list_per_page = 25

    fieldsets = (

        ("Paper Details", {
            "fields": (
                "paper_title",
                "author_name",
                "email",
                "keywords",
            )
        }),

        ("Abstract", {
            "fields": (
                "abstract",
            )
        }),

        ("Uploaded Paper", {
            "fields": (
                "paper_pdf",
            )
        }),

        ("Review", {
            "fields": (
                "status",
            )
        }),

        ("Submission Info", {
            "fields": (
                "submitted_at",
            )
        }),

    )

    def status_badge(self, obj):

        colors = {
            "Submitted": "#0d6efd",
            "Under Review": "#ffc107",
            "Accepted": "#198754",
            "Rejected": "#dc3545",
        }

        return format_html(
            '<span style="background:{};color:white;padding:6px 14px;border-radius:20px;font-weight:bold;">{}</span>',
            colors.get(obj.status, "#6c757d"),
            obj.status,
        )

    status_badge.short_description = "Status"
# =====================================================
# ANNOUNCEMENTS
# =====================================================

@admin.register(Announcement)
class AnnouncementAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "created_at",
    )

    search_fields = (
        "title",
        "description",
    )

    ordering = (
        "-created_at",
    )

    readonly_fields = (
        "created_at",
    )

    date_hierarchy = "created_at"

    list_per_page = 20

    fieldsets = (

        ("Announcement", {
            "fields": (
                "title",
                "description",
            )
        }),

        ("Information", {
            "fields": (
                "created_at",
            )
        }),

    )


# =====================================================
# CONTACT MESSAGES
# =====================================================

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
        "message",
    )

    ordering = (
        "-created_at",
    )

    readonly_fields = (
        "created_at",
    )

    date_hierarchy = "created_at"

    list_per_page = 30

    fieldsets = (

        ("Sender Details", {
            "fields": (
                "name",
                "email",
            )
        }),

        ("Message", {
            "fields": (
                "subject",
                "message",
            )
        }),

        ("Information", {
            "fields": (
                "created_at",
            )
        }),

    )


# =====================================================
# BROADCAST MESSAGES
# =====================================================

@admin.register(BroadcastMessage)
class BroadcastMessageAdmin(admin.ModelAdmin):

    list_display = (
        "subject",
        "send_email",
        "send_whatsapp",
        "status",
        "created_at",
    )

    list_filter = (
        "status",
        "send_email",
        "send_whatsapp",
    )

    search_fields = (
        "subject",
        "message",
    )

    ordering = (
        "-created_at",
    )

    readonly_fields = (
        "created_at",
    )

    date_hierarchy = "created_at"

    list_per_page = 25

    fieldsets = (

        ("Broadcast", {
            "fields": (
                "subject",
                "message",
            )
        }),

        ("Delivery Options", {
            "fields": (
                "send_email",
                "send_whatsapp",
                "status",
            )
        }),

        ("Information", {
            "fields": (
                "created_at",
            )
        }),

    )


# =====================================================
# HOME PAGE STATISTICS
# =====================================================

@admin.register(Statistics)
class StatisticsAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "display_order",
        "icon",
        "value",
    )

    list_editable = (
        "display_order",
        "value",
    )

    search_fields = (
        "title",
    )

    ordering = (
        "display_order",
    )

    list_per_page = 20

    fieldsets = (

        ("Statistic", {
            "fields": (
                "title",
                "value",
                "icon",
                "display_order",
            )
        }),

    )
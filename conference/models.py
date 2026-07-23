from django.db import models
# ==========================================
# WEBSITE SETTINGS
# ==========================================

class WebsiteSettings(models.Model):
    conference_name = models.CharField(max_length=250)
    short_name = models.CharField(max_length=100)
    organization = models.CharField(max_length=250)
    department = models.CharField(max_length=250)

    hero_heading = models.CharField(max_length=250)
    hero_subtitle = models.TextField()

    conference_date = models.CharField(max_length=100)
    venue = models.CharField(max_length=250)

    email = models.EmailField()
    phone = models.CharField(max_length=30)

    address = models.TextField()

    website = models.URLField(blank=True)

    facebook = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)
    twitter = models.URLField(blank=True)
    instagram = models.URLField(blank=True)

    primary_color = models.CharField(
        max_length=20,
        default="#0d6efd"
    )

    secondary_color = models.CharField(
        max_length=20,
        default="#0a2f66"
    )

    conference_logo = models.ImageField(
        upload_to="website/",
        blank=True,
        null=True
    )

    organization_logo = models.ImageField(
        upload_to="website/",
        blank=True,
        null=True
    )

    hero_image = models.ImageField(
        upload_to="website/",
        blank=True,
        null=True
    )

    favicon = models.ImageField(
        upload_to="website/",
        blank=True,
        null=True
    )

    copyright = models.CharField(
        max_length=300,
        default="© Conference"
    )

    def __str__(self):
        return self.conference_name


# ==========================================
# ABOUT
# ==========================================

class AboutConference(models.Model):

    title = models.CharField(max_length=200)

    description = models.TextField()

    vision = models.TextField(blank=True)

    mission = models.TextField(blank=True)

    image = models.ImageField(
        upload_to="about/",
        blank=True,
        null=True
    )

    def __str__(self):
        return self.title


# ==========================================
# TRACKS
# ==========================================

class ConferenceTrack(models.Model):

    name = models.CharField(max_length=200)

    description = models.TextField()

    icon = models.CharField(
        max_length=100,
        blank=True
    )

    def __str__(self):
        return self.name


# ==========================================
# IMPORTANT DATES
# ==========================================

class ImportantDate(models.Model):

    event = models.CharField(max_length=200)

    date = models.DateField()

    description = models.CharField(
        max_length=300,
        blank=True
    )

    class Meta:
        ordering = ['date']

    def __str__(self):
        return self.event


# ==========================================
# SPEAKERS
# ==========================================

class Speaker(models.Model):

    name = models.CharField(max_length=200)

    designation = models.CharField(max_length=200)

    organization = models.CharField(max_length=250)

    biography = models.TextField()

    photo = models.ImageField(
        upload_to="speakers/"
    )

    linkedin = models.URLField(blank=True)

    def __str__(self):
        return self.name


# ==========================================
# COMMITTEE
# ==========================================

class CommitteeMember(models.Model):

    name = models.CharField(max_length=200)

    designation = models.CharField(max_length=200)

    organization = models.CharField(max_length=250)

    photo = models.ImageField(
        upload_to="committee/",
        blank=True,
        null=True
    )

    def __str__(self):
        return self.name


# ==========================================
# GALLERY
# ==========================================

class Gallery(models.Model):

    title = models.CharField(max_length=200)

    image = models.ImageField(
        upload_to="gallery/"
    )

    uploaded_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.title


# ==========================================
# VENUE
# ==========================================

class VenueLocation(models.Model):

    name = models.CharField(max_length=200)

    address = models.TextField()

    google_map_link = models.URLField()

    image = models.ImageField(
        upload_to="venue/",
        blank=True,
        null=True
    )

    def __str__(self):
        return self.name


# ==========================================
# SCHEDULE
# ==========================================

class Schedule(models.Model):

    day = models.CharField(max_length=100)

    time = models.CharField(max_length=50)

    event = models.CharField(max_length=300)

    speaker = models.CharField(
        max_length=200,
        blank=True
    )

    venue = models.CharField(
        max_length=200,
        blank=True
    )

    def __str__(self):
        return f"{self.day} - {self.time}"


# ==========================================
# REGISTRATION
# ==========================================
class Registration(models.Model):

    CATEGORY = [
        ("Student", "Student"),
        ("Research Scholar", "Research Scholar"),
        ("Faculty", "Faculty"),
        ("Industry", "Industry"),
    ]

    GENDER = [
        ("Male", "Male"),
        ("Female", "Female"),
        ("Other", "Other"),
    ]

    PAYMENT = [
        ("Pending", "Pending"),
        ("Paid", "Paid"),
        ("Rejected", "Rejected"),
    ]

    full_name = models.CharField(max_length=150)

    email = models.EmailField(unique=True)

    phone = models.CharField(max_length=20)

    organization = models.CharField(max_length=250)

    designation = models.CharField(max_length=150, blank=True)

    country = models.CharField(max_length=100)

    city = models.CharField(max_length=100, blank=True)

    
    gender = models.CharField(
      max_length=20,
      choices=GENDER,
      blank=True,
      null=True
    )

    category = models.CharField(
        max_length=50,
        choices=CATEGORY
    )

    registration_fee = models.DecimalField(
       max_digits=10,
       decimal_places=2,
       default=0,
       blank=True,
       null=True
   )

    payment_status = models.CharField(
        max_length=20,
        choices=PAYMENT,
        default="Pending"
    )

    verified_by = models.CharField(
        max_length=100,
        blank=True
    )

    verified_date = models.DateTimeField(
        blank=True,
        null=True
   )

    payment_verified = models.BooleanField(
        default=False
  )

    transaction_id = models.CharField(
        max_length=150,
        blank=True
    )

    payment_receipt = models.FileField(
        upload_to="payment_receipts/",
        blank=True,
        null=True
    )

    remarks = models.TextField(blank=True)

    registered_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name

# ==========================================
# PAPER SUBMISSION
# ==========================================

class PaperSubmission(models.Model):

    STATUS = [

        ("Submitted", "Submitted"),

        ("Under Review", "Under Review"),

        ("Accepted", "Accepted"),

        ("Rejected", "Rejected"),

    ]

    paper_title = models.CharField(max_length=300)

    author_name = models.CharField(max_length=200)

    email = models.EmailField()

    abstract = models.TextField()

    keywords = models.CharField(
        max_length=400
    )

    paper_pdf = models.FileField(
        upload_to="papers/"
    )

    status = models.CharField(
        max_length=30,
        choices=STATUS,
        default="Submitted"
    )

    submitted_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.paper_title


# ==========================================
# ANNOUNCEMENTS
# ==========================================

class Announcement(models.Model):

    title = models.CharField(max_length=200)

    description = models.TextField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.title


# ==========================================
# CONTACT
# ==========================================

class ContactMessage(models.Model):

    name = models.CharField(max_length=100)

    email = models.EmailField()

    subject = models.CharField(max_length=200)

    message = models.TextField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.subject


# ==========================================
# BROADCAST
# ==========================================

class BroadcastMessage(models.Model):

    STATUS = [

        ("Pending", "Pending"),

        ("Sent", "Sent"),

        ("Failed", "Failed"),

    ]

    subject = models.CharField(max_length=200)

    message = models.TextField()

    send_email = models.BooleanField(default=True)

    send_whatsapp = models.BooleanField(default=False)

    status = models.CharField(
        max_length=20,
        choices=STATUS,
        default="Pending"
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.subject
# ==========================================
# HOME PAGE STATISTICS
# ==========================================

class Statistics(models.Model):

    title = models.CharField(max_length=100)

    value = models.PositiveIntegerField()

    icon = models.CharField(max_length=100)

    display_order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["display_order"]
        verbose_name_plural = "Statistics"

    def __str__(self):
        return self.title
# ==========================================
# REGISTRATION FEES
# ==========================================

class RegistrationFee(models.Model):

    CATEGORY = [
        ("Student", "Student"),
        ("Research Scholar", "Research Scholar"),
        ("Faculty", "Faculty"),
        ("Industry", "Industry"),
    ]

    category = models.CharField(
        max_length=50,
        choices=CATEGORY,
        unique=True
    )

    indian_fee = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    foreign_fee = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    currency = models.CharField(
        max_length=10,
        default="INR"
    )

    active = models.BooleanField(
        default=True
    )

    display_order = models.PositiveIntegerField(
        default=0
    )

    class Meta:
        ordering = ["display_order"]

    def __str__(self):
        return self.category


# ==========================================
# PAYMENT SETTINGS
# ==========================================

class PaymentSettings(models.Model):

    registration_deadline = models.DateField(
       blank=True,
        null=True
    )

    camera_ready_deadline = models.DateField(
       blank=True,
       null=True
   )

    early_bird_deadline = models.DateField(
       blank=True,
       null=True
    )

    upi_id = models.CharField(
        max_length=100,
        blank=True
    )

    qr_code = models.ImageField(
        upload_to="payment/",
        blank=True,
        null=True
    )

    account_name = models.CharField(
        max_length=200,
        blank=True
    )

    bank_name = models.CharField(
        max_length=200,
        blank=True
    )

    account_number = models.CharField(
        max_length=50,
        blank=True
    )

    ifsc_code = models.CharField(
        max_length=50,
        blank=True
    )

    swift_code = models.CharField(
        max_length=50,
        blank=True
    )

    support_email = models.EmailField(
        blank=True
    )

    payment_note = models.TextField(
        blank=True
    )

    def __str__(self):
        return "Payment Settings"
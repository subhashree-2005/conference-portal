from django.db import models


class VenueLocation(models.Model):
    name = models.CharField(max_length=200)

    address = models.TextField()

    google_map_link = models.URLField()

    def __str__(self):
        return self.name


class Registration(models.Model):
    full_name = models.CharField(max_length=100)

    email = models.EmailField()

    phone = models.CharField(max_length=20)

    organization = models.CharField(max_length=100)

    country = models.CharField(max_length=100)

    def __str__(self):
        return self.full_name


class PaperSubmission(models.Model):
    STATUS_CHOICES = [
        ('Submitted', 'Submitted'),
        ('Under Review', 'Under Review'),
        ('Accepted', 'Accepted'),
        ('Rejected', 'Rejected'),
    ]

    paper_title = models.CharField(max_length=200)

    author_name = models.CharField(max_length=100)

    email = models.EmailField()

    abstract = models.TextField()

    keywords = models.CharField(
        max_length=300,
        blank=True
    )

    paper_pdf = models.FileField(
        upload_to='papers/'
    )

    status = models.CharField(
        max_length=50,
        choices=STATUS_CHOICES,
        default='Submitted'
    )

    def __str__(self):
        return self.paper_title

class Speaker(models.Model):

    name = models.CharField(max_length=100)

    designation = models.CharField(max_length=200)

    organization = models.CharField(
        max_length=300,
        blank=True
    )

    biography = models.TextField(blank=True)

    photo = models.ImageField(
        upload_to='speakers/'
    )

    def __str__(self):
        return self.name


class Announcement(models.Model):
    title = models.CharField(max_length=200)

    description = models.TextField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.title


class Schedule(models.Model):
    time = models.CharField(max_length=50)

    event = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.time} - {self.event}"


class ConferenceSettings(models.Model):

    title = models.CharField(max_length=300)

    subtitle = models.TextField(blank=True)

    venue = models.CharField(max_length=300)

    start_date = models.DateField()

    end_date = models.DateField()

    banner_image = models.ImageField(
        upload_to='conference_banner/',
        blank=True,
        null=True
    )

class Meta:
    verbose_name = "Conference Settings"
    verbose_name_plural = "Conference Settings"

    def __str__(self):
        return self.title
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
class Gallery(models.Model):

    title = models.CharField(max_length=200)

    image = models.ImageField(
        upload_to='gallery/'
    )

    uploaded_at = models.DateTimeField(
        auto_now_add=True
    )
class Meta:
    verbose_name = "Gallery"
    verbose_name_plural = "Gallery"
    
    def __str__(self):
        return self.title
class ConferenceTrack(models.Model):

    name = models.CharField(max_length=200)

    description = models.TextField()

    def __str__(self):
        return self.name

class BroadcastMessage(models.Model):
    STATUS_CHOICES = [
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
        choices=STATUS_CHOICES,
        default="Pending",
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject
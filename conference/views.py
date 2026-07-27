from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required
from django.core.mail import send_mail
from django.core import signing
from django.conf import settings as django_settings

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
    PaperSubmission,
    Announcement,
    ContactMessage,
    BroadcastMessage,
    Statistics,
    RegistrationFee,
    PaymentSettings,
)

from .forms import (
    RegistrationForm,
    PaperSubmissionForm,
    ContactForm,
)

SIGNING_SALT = "conference.payment-access"


def make_payment_token(registration_id):
    """Creates a tamper-proof token so a registrant's emailed payment link
    keeps working even from a different browser/device than the one they
    registered on, without letting strangers guess other people's links."""
    return signing.dumps(registration_id, salt=SIGNING_SALT)


def verify_payment_token(token, registration_id):
    try:
        return signing.loads(
            token, salt=SIGNING_SALT, max_age=60 * 60 * 24 * 30
        ) == registration_id
    except signing.BadSignature:
        return False


# ==================================================
# HOME PAGE
# ==================================================

def home(request):

    settings = WebsiteSettings.objects.first()

    context = {

        "settings": settings,

        "about": AboutConference.objects.first(),

        "tracks": ConferenceTrack.objects.all(),

        "important_dates": ImportantDate.objects.all(),

        "speakers": Speaker.objects.all(),

        "committee": CommitteeMember.objects.all(),

        "gallery": Gallery.objects.all(),

        "venue": VenueLocation.objects.first(),

        "schedule": Schedule.objects.all(),

        "announcements": Announcement.objects.order_by("-created_at"),

        "statistics": Statistics.objects.all(),

    }

    return render(request, "home.html", context)


# ==================================================
# REGISTRATION
# ==================================================

def register(request):

    settings = WebsiteSettings.objects.first()

    registration_fees = RegistrationFee.objects.filter(
        active=True
    )

    payment = PaymentSettings.objects.first()

    if request.method == "POST":

        form = RegistrationForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():

            registration = form.save(commit=False)

            try:

                fee = RegistrationFee.objects.get(
                    category=registration.category,
                    active=True
                )

                if registration.country.lower() == "india":
                 registration.registration_fee = fee.indian_fee
                else:
                 registration.registration_fee = fee.foreign_fee

            except RegistrationFee.DoesNotExist:

                registration.registration_fee = 0

            registration.save()

            # ==========================
            # SEND CONFIRMATION EMAIL
            # ==========================

            try:

                payment_link = request.build_absolute_uri(
                    f"/payment/{registration.id}/?t={make_payment_token(registration.id)}"
                )

                send_mail(

                    subject="Conference Registration Successful",

                    message=f"""
Dear {registration.full_name},

Your registration has been received successfully.

-----------------------------------

Registration Details

Name :
{registration.full_name}

Email :
{registration.email}

Organization :
{registration.organization}

Category :
{registration.category}

Registration Fee :
₹{registration.registration_fee}

Payment Status :
{registration.payment_status}

-----------------------------------

Complete your payment / upload your receipt here (keep this link private,
it is unique to you):
{payment_link}

Please keep this email for future reference.

Thank you for registering.

Conference Organizing Committee
""",

                    from_email=django_settings.DEFAULT_FROM_EMAIL,

                    recipient_list=[
                        registration.email
                    ],

                    fail_silently=False,

                )

            except Exception as e:

                print("Email Error :", e)

            messages.success(

                request,

                "Registration completed successfully. A confirmation email has been sent."

            )

            # Remember this registration in the visitor's own browser session
            # so the payment page (below) can confirm it's really them.
            request.session["registration_id"] = registration.id

            token = make_payment_token(registration.id)
            return redirect(f"/payment/{registration.id}/?t={token}")

    else:

        form = RegistrationForm()

    context = {

        "form": form,

        "settings": settings,

        "fees": registration_fees,

        "payment": payment,

    }

    return render(

        request,

        "register.html",

        context,

    )

# ==================================================
# PAYMENT PAGE
# ==================================================

def payment(request, pk):

    # Only the person who just registered (their session remembers the id)
    # or a logged-in staff member may view/edit this payment page. This
    # stops strangers from browsing /payment/1/, /payment/2/, ... and
    # seeing or tampering with other people's registration + payment info.
    token_ok = verify_payment_token(request.GET.get("t", ""), pk)

    if (
        request.session.get("registration_id") != pk
        and not token_ok
        and not (request.user.is_authenticated and request.user.is_staff)
    ):
        messages.error(
            request,
            "That payment page isn't accessible from this browser/session. "
            "Please use the link from your confirmation email, or register again."
        )
        return redirect("register")

    if token_ok:
        request.session["registration_id"] = pk

    registration = get_object_or_404(Registration, id=pk)

    payment = PaymentSettings.objects.first()

    fees = RegistrationFee.objects.filter(active=True)

    if request.method == "POST":

        registration.transaction_id = request.POST.get("transaction_id")

        uploaded_receipt = request.FILES.get("payment_receipt")
        if uploaded_receipt:
            try:
                from .forms import validate_receipt
                validate_receipt(uploaded_receipt)
                registration.payment_receipt = uploaded_receipt
            except Exception as e:
                messages.error(request, str(e))
                return redirect(f"/payment/{registration.id}/")

        registration.payment_status = "Pending"

        registration.payment_verified = False

        registration.save()

        messages.success(
            request,
            "Payment details submitted successfully. Your payment will be verified by the administrator."
        )

        return redirect("payment", pk=registration.id)

    context = {

        "registration": registration,

        "payment": payment,

        "fees": fees,

        "settings": WebsiteSettings.objects.first(),

    }

    return render(
        request,
        "payment.html",
        context,
    )

# ==================================================
# PAPER SUBMISSION
# ==================================================

def submit_paper(request):

    if request.method == "POST":

        form = PaperSubmissionForm(

            request.POST,

            request.FILES,

        )

        if form.is_valid():

            paper = form.save(commit=False)

            # ==========================
            # CHECK DUPLICATE PAPER
            # ==========================

            duplicate = PaperSubmission.objects.filter(

                paper_title=paper.paper_title,

                email=paper.email

            ).exists()

            if duplicate:

                messages.error(

                    request,

                    "This paper has already been submitted."

                )

                return redirect("submit_paper")

            # ==========================
            # SAVE PAPER
            # ==========================

            paper.save()

            # ==========================
            # SEND CONFIRMATION EMAIL
            # ==========================

            try:

                send_mail(

                    subject="Paper Submission Successful",

                    message=f"""
Dear {paper.author_name},

Your paper has been submitted successfully.

---------------------------------------

Paper Details

Title :
{paper.paper_title}

Author :
{paper.author_name}

Email :
{paper.email}

Current Status :
{paper.status}

---------------------------------------

Your paper will now be reviewed by our Technical Committee.

You will receive another email once the review process is completed.

Thank you.

Conference Organizing Committee
""",

                    from_email=django_settings.EMAIL_HOST_USER,

                    recipient_list=[paper.email],

                    fail_silently=False,

                )

            except Exception as e:

                print("Paper Email Error :", e)

            messages.success(

                request,

                "Paper submitted successfully. Confirmation email sent."

            )

            return redirect("submit_paper")

    else:

        form = PaperSubmissionForm()

    context = {

        "form": form,

        "settings": WebsiteSettings.objects.first(),

    }

    return render(

        request,

        "submit_paper.html",

        context,

    )
# ==================================================
# CONTACT
# ==================================================

def contact(request):

    settings = WebsiteSettings.objects.first()

    if request.method == "POST":

        form = ContactForm(request.POST)

        if form.is_valid():

            contact = form.save()

            # Send acknowledgement email

            try:

                send_mail(

                    subject="We received your message",

                    message=f"""
Dear {contact.name},

Thank you for contacting us.

We have received your message regarding:

{contact.subject}

Our organizing committee will respond to you as soon as possible.

Regards,
Conference Organizing Committee
""",

                    from_email=django_settings.EMAIL_HOST_USER,

                    recipient_list=[contact.email],

                    fail_silently=False,

                )

            except Exception as e:

                print("Contact Email Error :", e)

            messages.success(

                request,

                "Your message has been sent successfully."

            )

            return redirect("contact")

    else:

        form = ContactForm()

    return render(

        request,

        "contact.html",

        {

            "form": form,

            "settings": settings,

        },

    )


# ==================================================
# DASHBOARD
# ==================================================

@staff_member_required
def dashboard(request):

    papers = PaperSubmission.objects.all()

    registrations = Registration.objects.all()

    context = {

        "paper_count": papers.count(),

        "accepted": papers.filter(status="Accepted").count(),

        "review": papers.filter(status="Under Review").count(),

        "rejected": papers.filter(status="Rejected").count(),

        "registration_count": registrations.count(),

        "paid_registration": registrations.filter(
            payment_status="Paid"
        ).count(),

        "pending_registration": registrations.filter(
            payment_status="Pending"
        ).count(),

        "papers": papers,

        "registrations": registrations,

        "announcements": Announcement.objects.order_by("-created_at")[:5],

    }

    return render(

        request,

        "dashboard.html",

        context,

    )


# ==================================================
# BROADCAST
# ==================================================

@staff_member_required
def broadcast(request):

    broadcasts = BroadcastMessage.objects.order_by(

        "-created_at"

    )

    if request.method == "POST":

        subject = request.POST.get("subject")

        message = request.POST.get("message")

        BroadcastMessage.objects.create(

            subject=subject,

            message=message,

            send_email=True,

            send_whatsapp=False,

            status="Sent",

        )

        # Send email to all registered participants

        emails = list(

            Registration.objects.values_list(

                "email",

                flat=True

            )

        )

        if emails:

            try:

                send_mail(

                    subject,

                    message,

                    django_settings.EMAIL_HOST_USER,

                    emails,

                    fail_silently=False,

                )

            except Exception as e:

                print("Broadcast Email Error :", e)

        messages.success(

            request,

            "Broadcast sent successfully."

        )

        return redirect("broadcast")

    return render(

        request,

        "broadcast.html",

        {

            "broadcasts": broadcasts,

        },

    )
# ==================================================
# DASHBOARD PAGES
# ==================================================

@staff_member_required
def registration_list(request):
    return redirect("/admin/conference/registration/")


@staff_member_required
def paper_list(request):
    return redirect("/admin/conference/papersubmission/")


@staff_member_required
def speaker_list(request):
    return redirect("/admin/conference/speaker/")


@staff_member_required
def committee_list(request):
    return redirect("/admin/conference/committeemember/")


@staff_member_required
def gallery_list(request):
    return redirect("/admin/conference/gallery/")


@staff_member_required
def schedule_list(request):
    return redirect("/admin/conference/schedule/")


@staff_member_required
def venue_list(request):
    return redirect("/admin/conference/venuelocation/")


@staff_member_required
def announcement_list(request):
    return redirect("/admin/conference/announcement/")


@staff_member_required
def website_settings(request):
    return redirect("/admin/conference/websitesettings/")
from django.shortcuts import render, redirect
from .forms import RegistrationForm, PaperSubmissionForm, ContactForm
from .models import (
    Speaker,
    Announcement,
    Registration,
    PaperSubmission,
    Schedule,
    VenueLocation,
    ContactMessage,
    ConferenceTrack,
    Gallery
)

def home(request):

    speakers = Speaker.objects.all()

    announcements = Announcement.objects.all().order_by('-created_at')[:5]

    participant_count = Registration.objects.count()
    paper_count = PaperSubmission.objects.count()
    speaker_count = Speaker.objects.count()
    announcement_count = Announcement.objects.count()

    schedules = Schedule.objects.all()
    locations = VenueLocation.objects.all()

    tracks = ConferenceTrack.objects.all()

    gallery = Gallery.objects.all()

    papers = PaperSubmission.objects.all().order_by('-id')[:10]

    return render(request, 'home.html', {

        'locations': locations,

        'speakers': speakers,

        'announcements': announcements,

        'participant_count': participant_count,

        'paper_count': paper_count,

        'speaker_count': speaker_count,

        'announcement_count': announcement_count,

        'schedules': schedules,

        'tracks': tracks,

        'gallery': gallery,

        'papers': papers,
    })


def register(request):

    if request.method == "POST":
        form = RegistrationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/')

    else:
        form = RegistrationForm()

    return render(request, 'register.html', {'form': form})


def submit_paper(request):

    if request.method == "POST":
        form = PaperSubmissionForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('/')

    else:
        form = PaperSubmissionForm()

    return render(request, 'submit_paper.html', {'form': form})


def dashboard(request):

    participant_count = Registration.objects.count()
    paper_count = PaperSubmission.objects.count()
    speaker_count = Speaker.objects.count()
    announcement_count = Announcement.objects.count()

    return render(request, 'dashboard.html', {
        'participant_count': participant_count,
        'paper_count': paper_count,
        'speaker_count': speaker_count,
        'announcement_count': announcement_count
    })
def contact_message(request):

    if request.method == "POST":

        form = ContactForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect('/')

    return redirect('/')
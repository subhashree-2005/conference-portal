from django import forms
from .models import Registration, PaperSubmission
from .models import ContactMessage

class RegistrationForm(forms.ModelForm):

    class Meta:

        model = Registration

        fields = [
            'full_name',
            'email',
            'phone',
            'organization',
            'country'
        ]
class PaperSubmissionForm(forms.ModelForm):

    class Meta:

        model = PaperSubmission

        fields = [
            'paper_title',
            'author_name',
            'email',
            'abstract',
            'paper_pdf'
        ]
class ContactForm(forms.ModelForm):

    class Meta:

        model = ContactMessage

        fields = [
            'name',
            'email',
            'subject',
            'message'
        ]
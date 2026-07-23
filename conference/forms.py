from django import forms
from django.core.exceptions import ValidationError

from .models import (
    Registration,
    PaperSubmission,
    ContactMessage
)

MAX_UPLOAD_MB = 10


def validate_pdf(value):
    if not value.name.lower().endswith(".pdf"):
        raise ValidationError("Only PDF files are accepted.")
    if value.size > MAX_UPLOAD_MB * 1024 * 1024:
        raise ValidationError(f"File must be smaller than {MAX_UPLOAD_MB}MB.")


def validate_receipt(value):
    allowed = (".pdf", ".jpg", ".jpeg", ".png")
    if not value.name.lower().endswith(allowed):
        raise ValidationError("Only PDF, JPG or PNG files are accepted.")
    if value.size > MAX_UPLOAD_MB * 1024 * 1024:
        raise ValidationError(f"File must be smaller than {MAX_UPLOAD_MB}MB.")


# ==========================================
# REGISTRATION FORM
# ==========================================

class RegistrationForm(forms.ModelForm):

    class Meta:
        model = Registration

        fields = [
            "full_name",
            "email",
            "phone",
            "organization",
            "country",
            "category",
            "designation",
            "city",
            "gender",
            "transaction_id",
            "payment_receipt"
        ]

        widgets = {

            "full_name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Full Name"
            }),

            "email": forms.EmailInput(attrs={
                "class": "form-control",
                "placeholder": "Email Address"
            }),

            "phone": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Phone Number"
            }),

            "organization": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "College / Organization"
            }),

            "country": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Country"
            }),

            "category": forms.Select(attrs={
                "class": "form-select"
            }),
            "designation": forms.TextInput(
               attrs={
                "class":"form-control",
                "placeholder":"Designation"
               }
            ),

            "city": forms.TextInput(
               attrs={
                  "class":"form-control",
                  "placeholder":"City"
               }
            ),

            "gender": forms.Select(
                attrs={
                   "class":"form-select"
                }
           ),

            "transaction_id": forms.TextInput(
                attrs={
                   "class":"form-control",
                    "placeholder":"Transaction ID"
              }
           ),

            "payment_receipt": forms.ClearableFileInput(
                 attrs={
                    "class":"form-control"
            }
           ),
        }

    def clean_payment_receipt(self):
        f = self.cleaned_data.get("payment_receipt")
        if f:
            validate_receipt(f)
        return f


# ==========================================
# PAPER SUBMISSION FORM
# ==========================================

class PaperSubmissionForm(forms.ModelForm):

    class Meta:

        model = PaperSubmission

        fields = [
            "paper_title",
            "author_name",
            "email",
            "abstract",
            "keywords",
            "paper_pdf",
        ]

        widgets = {

            "paper_title": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Paper Title"
            }),

            "author_name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Author Name"
            }),

            "email": forms.EmailInput(attrs={
                "class": "form-control",
                "placeholder": "Email"
            }),

            "abstract": forms.Textarea(attrs={
                "class": "form-control",
                "rows": 6,
                "placeholder": "Abstract"
            }),

            "keywords": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "AI, Machine Learning, FPGA"
            }),

            "paper_pdf": forms.ClearableFileInput(attrs={
                "class": "form-control"
            }),

        }

    def clean_paper_pdf(self):
        f = self.cleaned_data.get("paper_pdf")
        if f:
            validate_pdf(f)
        return f


# ==========================================
# CONTACT FORM
# ==========================================

class ContactForm(forms.ModelForm):

    class Meta:

        model = ContactMessage

        fields = [
            "name",
            "email",
            "subject",
            "message",
        ]

        widgets = {

            "name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Full Name"
            }),

            "email": forms.EmailInput(attrs={
                "class": "form-control",
                "placeholder": "Email Address"
            }),

            "subject": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Subject"
            }),

            "message": forms.Textarea(attrs={
                "class": "form-control",
                "rows": 6,
                "placeholder": "Write your message..."
            }),

        }
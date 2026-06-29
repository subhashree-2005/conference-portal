import requests

from django.conf import settings
from django.core.mail import send_mail

from .models import Registration


# ---------------- EMAIL ---------------- #

def send_email_to_all(subject, message):

    emails = Registration.objects.exclude(email="").values_list(
        "email",
        flat=True
    )

    emails = list(emails)

    if not emails:
        return

    try:
        send_mass_mail(
            (
                (
                    subject,
                    message,
                    settings.EMAIL_HOST_USER,
                    emails,
                ),
            ),
            fail_silently=True,
        )

    except Exception as e:
        print(e)

# ---------------- WHATSAPP ---------------- #

def send_whatsapp_to_all(message):

    phones = list(
        Registration.objects.exclude(phone="").values_list(
            "phone",
            flat=True
        )
    )

    if not phones:
        print("No phone numbers found.")
        return

    url = (
        f"https://7107.api.greenapi.com/"
        f"waInstance{settings.GREEN_API_ID_INSTANCE}/"
        f"sendMessage/"
        f"{settings.GREEN_API_TOKEN}"
    )

    for phone in phones:

        phone = str(phone)

        # Remove spaces and symbols
        phone = phone.replace("+", "")
        phone = phone.replace("-", "")
        phone = phone.replace(" ", "")

        # Remove leading zero
        if phone.startswith("0"):
            phone = phone[1:]

        # Add India country code if missing
        if len(phone) == 10:
            phone = "91" + phone

        payload = {
            "chatId": f"{phone}@c.us",
            "message": message
        }

        try:

            response = requests.post(url, json=payload)

            print(f"{phone} -> {response.status_code}")
            print(response.text)

        except Exception as e:

            print(f"WhatsApp Error ({phone}): {e}")
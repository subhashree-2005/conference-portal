import requests

from django.conf import settings
from django.core.mail import send_mass_mail

from .models import Registration


# ---------------- EMAIL ---------------- #

def send_email_to_all(subject, message):

    emails = list(
        Registration.objects.exclude(email="").values_list(
            "email",
            flat=True
        )
    )

    print("EMAILS:", emails)

    if not emails:
        print("No emails found.")
        return

    print("Trying to send email...")

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
            fail_silently=False,
        )

        print("EMAIL SENT SUCCESSFULLY")

    except Exception as e:
        import traceback
        traceback.print_exc()

    

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
        f"https://api.green-api.com/"
        f"waInstance{settings.GREEN_API_ID_INSTANCE}/"
        f"sendMessage/"
        f"{settings.GREEN_API_TOKEN}"
    )

    for phone in phones:

        phone = str(phone)

        phone = phone.replace("+", "")
        phone = phone.replace("-", "")
        phone = phone.replace(" ", "")

        if phone.startswith("0"):
            phone = phone[1:]

        if len(phone) == 10:
            phone = "91" + phone

        payload = {
            "chatId": f"{phone}@c.us",
            "message": message
        }

        try:

            response = requests.post(
                url,
                json=payload,
                timeout=20
            )

            print(f"{phone} -> {response.status_code}")

        except Exception as e:

            print(f"WhatsApp Error ({phone}): {e}")
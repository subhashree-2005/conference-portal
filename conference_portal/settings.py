from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent

# -----------------------------
# Security
# -----------------------------
SECRET_KEY = os.environ.get(
    "SECRET_KEY",
    "django-insecure-local-development-key"
)

DEBUG = os.environ.get("DEBUG", "True") == "True"

ALLOWED_HOSTS = [
    "127.0.0.1",
    "localhost",
    "conference-portal-sqa5.onrender.com",
]

# -----------------------------
# Installed Apps
# -----------------------------
INSTALLED_APPS = [
    "jazzmin",

    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    "conference",
]

# -----------------------------
# Middleware
# -----------------------------
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "conference_portal.urls"

# -----------------------------
# Templates
# -----------------------------
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "conference/templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "conference_portal.wsgi.application"

# -----------------------------
# Database
# -----------------------------
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# -----------------------------
# Password Validation
# -----------------------------
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# -----------------------------
# Internationalization
# -----------------------------
LANGUAGE_CODE = "en-us"

TIME_ZONE = "Asia/Kolkata"

USE_I18N = True

USE_TZ = True

# -----------------------------
# Static Files
# -----------------------------
STATIC_URL = "static/"

STATICFILES_DIRS = [
    BASE_DIR / "conference" / "static",
]

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# -----------------------------
# Email Configuration
# -----------------------------
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"

EMAIL_HOST = "smtp.gmail.com"

EMAIL_PORT = 587

EMAIL_USE_TLS = True

EMAIL_HOST_USER = os.environ.get("subhashreeaich55@gmail.com")

EMAIL_HOST_PASSWORD = os.environ.get("easw tveu xbct ddxf")

DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

# -----------------------------
# Green API
# -----------------------------
GREEN_API_ID_INSTANCE = os.environ.get("7107666703")

GREEN_API_TOKEN = os.environ.get("f0b2596796914d28b43b6deb0931fc97bc94520b3b8143a2a7")

JAZZMIN_SETTINGS = {

    "site_title": "Conference Admin",

    "site_header": "Conference Management System",

    "site_brand": "Conference CMS",

    "welcome_sign": "Welcome to Conference Management System",

    "copyright": "© 2026 Conference Portal",

    "show_sidebar": True,

    "navigation_expanded": True,

    "hide_apps": [],

    "hide_models": [],

    "icons": {
        "auth.User": "fas fa-user",
        "auth.Group": "fas fa-users",

        "conference.registration": "fas fa-user-check",
        "conference.papersubmission": "fas fa-file-alt",
        "conference.speaker": "fas fa-microphone",
        "conference.schedule": "fas fa-calendar-alt",
        "conference.announcement": "fas fa-bullhorn",
        "conference.gallery": "fas fa-images",
        "conference.contactmessage": "fas fa-envelope",
        "conference.broadcastmessage": "fas fa-paper-plane",
        "conference.venuelocation": "fas fa-map-marker-alt",
        "conference.conferencetrack": "fas fa-layer-group",
        "conference.conferencesettings": "fas fa-cogs",
    },

    "topmenu_links": [
        {"name": "Home", "url": "/", "permissions": ["auth.view_user"]},
    ],
}
JAZZMIN_UI_TWEAKS = {

    "theme": "flatly",

    "dark_mode_theme": "darkly",

    "navbar": "navbar-primary",

    "sidebar": "sidebar-dark-primary",

    "accent": "accent-primary",

    "brand_colour": "navbar-primary",

    "sidebar_nav_small_text": False,

    "sidebar_disable_expand": False,

}
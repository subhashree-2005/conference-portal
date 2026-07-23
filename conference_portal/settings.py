from pathlib import Path
import os
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent

# Loads variables from a local .env file (gitignored) into os.environ.
# On Render, environment variables are set in the dashboard instead, and
# this call is a harmless no-op if no .env file exists.
load_dotenv(BASE_DIR / ".env")

# -----------------------------
# Security
# -----------------------------
# In production (Render) SECRET_KEY MUST be set as an environment variable.
# The fallback below only exists so `manage.py` commands still work on a
# fresh local checkout before you've created a .env file.
SECRET_KEY = os.environ.get(
    "SECRET_KEY",
    "django-insecure-local-development-key-change-me"
)

# DEBUG must be OFF in production. Default is now False and safe;
# set DEBUG=True in your local .env only.
DEBUG = os.environ.get("DEBUG", "False") == "True"

ALLOWED_HOSTS = os.environ.get(
    "ALLOWED_HOSTS",
    "127.0.0.1,localhost"
).split(",")

# Needed so Django trusts HTTPS POST requests (forms, admin login) coming
# through Render's proxy - without this you can get "CSRF verification failed".
CSRF_TRUSTED_ORIGINS = [
    origin.strip()
    for origin in os.environ.get(
        "CSRF_TRUSTED_ORIGINS",
        "https://*.onrender.com"
    ).split(",")
    if origin.strip()
]

# Tell Django it's behind an HTTPS-terminating proxy (Render/most PaaS)
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

if not DEBUG:
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    SECURE_SSL_REDIRECT = os.environ.get("SECURE_SSL_REDIRECT", "True") == "True"
    SECURE_HSTS_SECONDS = int(os.environ.get("SECURE_HSTS_SECONDS", "3600"))

# -----------------------------
# Installed Apps
# -----------------------------
INSTALLED_APPS = [
    "jazzmin",

    'django.contrib.admin',

    'django.contrib.auth',

    'django.contrib.contenttypes',

    'django.contrib.sessions',

    'django.contrib.messages',

    'django.contrib.staticfiles',

    'conference',

]

# -----------------------------
# Middleware
# -----------------------------
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",

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

        'BACKEND':
        'django.template.backends.django.DjangoTemplates',

        'DIRS': [

            BASE_DIR / 'conference/templates',

        ],

        'APP_DIRS': True,

        'OPTIONS': {

            'context_processors': [

                'django.template.context_processors.request',

                'django.contrib.auth.context_processors.auth',

                'django.contrib.messages.context_processors.messages',

                'conference.context_processors.conference_settings',

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
    BASE_DIR / 'conference/static',
]
STATIC_ROOT = BASE_DIR / 'staticfiles'

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Any view protected with @login_required / @staff_member_required will
# redirect here if the visitor isn't logged in.
LOGIN_URL = "/admin/login/"

# -----------------------------
# Email Configuration
# -----------------------------
# NEVER hardcode real credentials here. Set these as environment variables
# (locally in a .env file that is gitignored, and in Render's dashboard for
# production). EMAIL_HOST_PASSWORD must be a Gmail "App Password", not your
# normal Gmail login password.
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"

EMAIL_HOST = os.environ.get("EMAIL_HOST", "smtp.gmail.com")

EMAIL_PORT = int(os.environ.get("EMAIL_PORT", "587"))

EMAIL_USE_TLS = os.environ.get("EMAIL_USE_TLS", "True") == "True"

EMAIL_HOST_USER = os.environ.get("EMAIL_HOST_USER", "")

EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_HOST_PASSWORD", "")

DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

# -----------------------------
# Green API
# -----------------------------
GREEN_API_ID_INSTANCE = os.environ.get("GREEN_API_ID_INSTANCE")
GREEN_API_TOKEN = os.environ.get("GREEN_API_TOKEN")

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
        "conference.websitesettings": "fas fa-cogs",
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
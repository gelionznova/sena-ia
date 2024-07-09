import os
import datetime
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'tu_valor_predeterminado')
# DEBUG = True

# deploy
DEBUG = False

# ALLOWED_HOSTS = ["127.0.0.1", "localhost"]
ALLOWED_HOSTS = ["gpsdjango-61ff97537fca.herokuapp.com"]

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',    
    "rest_framework",
    "drf_yasg",
    "corsheaders",
    "django_filters",
    "psycopg2",    
    "users",
    "codeqr",
    "points",
    "pays",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = 'gps.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'gps.wsgi.application'

# BASE DE DATO SQLITE
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}



AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    )
}

LANGUAGE_CODE = "es-es"
TIME_ZONE = 'America/Bogota'
USE_TZ = True
USE_I18N = True
USE_L10N = True
USE_TZ = True

STATIC_URL = "/static/"
MEDIA_URL = "/uploads/"
MEDIA_ROOT = os.path.join(BASE_DIR, "uploads")

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = "users.User"


CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True  

CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True

SIMPLE_JWT = {"ACCESS_TOKEN_LIFETIME": datetime.timedelta(days=120)}

STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
STATIC_TMP = os.path.join(BASE_DIR, "static")
os.makedirs(STATIC_TMP, exist_ok=True)
os.makedirs(STATIC_ROOT, exist_ok=True)

STATICFILES_DIRS = (os.path.join(BASE_DIR, "static"),)
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

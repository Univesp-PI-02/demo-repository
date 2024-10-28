from .settings import *
import os

WIBBLE2 = 'Wibble2'


#é aqui que informo o meu domínio
#CSRF_TRUSTED_ORIGINS = ['https://*'] 
#CSRF_TRUSTED_ORIGINS = ['https://youdomain.azurewebsites.net']

#CSRF_TRUSTED_ORIGINS = ['https://equilibreapp.azurewebsites.net']
# TO-ADD -- uncomment

#add the next middleware for whitenoise

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    # Enables whitenoise for serving static files
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

#TO-DO add the static files
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

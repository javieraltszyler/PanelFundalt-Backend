from .base import *
import os

env.read_env(os.path.join(BASE_DIR, '.env_prod'))

SECRET_KEY = env('SECRET_KEY')
DEBUG = env.bool('DEBUG', default=False) #Cambiar a variable 'DJANGO_DEBUG'
ALLOWED_HOSTS = env.list('ALLOWED_HOSTS', default=[])

DATABASES = {
    'default': {
        'ENGINE': env('DB_ENGINE'),
        'NAME': env('DB_NAME'),
        'USER': env('DB_USER'),
        'PASSWORD': env('DB_PASSWORD'),
        'HOST': env('DB_HOST'),
        'PORT': env('DB_PORT'),
    }
}


# Configuraciones de SSL/HTTPS comentadas por el momento
# SECURE_SSL_REDIRECT = True
# SECURE_HSTS_SECONDS = 31536000  # 1 año
# SECURE_HSTS_INCLUDE_SUBDOMAINS = True
# SECURE_HSTS_PRELOAD = True
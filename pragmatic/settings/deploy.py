from .base import *

import environ

# docker의 secret에 설정한 값이 container의 파일로 저장되는데 이 값을 가져옴.
def read_secret(secret_name):
    file = open('/run/secrets/' + secret_name)
    secret = file.read().strip()
    file.close()
    return secret

environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

env = environ.Env(
    DEBUG=(bool, False)
)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
#SECRET_KEY = env('SECRET_KEY')
SECRET_KEY = read_secret('DJANGO_SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django',
        'USER': 'django',
        #'PASSWORD': read_secret('MYSQL_PASSWORD'),
        'PASSWORD': 'kwon0711',
        'HOST': 'mariadb', # 도커 네트워크 안에서 container 이름을 통해 접근하므로 중요.
        'PORT': '3306',
    }
}

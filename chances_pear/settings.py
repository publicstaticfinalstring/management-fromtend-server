

import os
import sys
from pathlib import Path


# Build paths inside the project like this: BASE_DIR / 'subdir'.
# BASE_DIR = Path(__file__).resolve().parent.parent
BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE_DIR))  # 将项目根目录添加到系统路径中
sys.path.insert(0,Path(BASE_DIR).joinpath('apps').as_posix())  # 将apps子目录添加到系统路径中
sys.path.insert(0,Path(BASE_DIR).joinpath('extra_apps').as_posix())  # 将extra_apps子目录添加到系统路径中


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-z)=jq97_fhmv+6^krgu2-)zeeb6nq*4kdmf=*40ggh(qi2@n4d"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']
SESSION_COOKIE_SAMESITE = 'None'
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SAMESITE = 'None'
CSRF_COOKIE_SECURE = True

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'xadmin',  # django-xadmin
    'DjangoUeditor',
    'crispy_forms',  # django-crispy-forms
    'import_export',  # django-import-export
    'reversion',  # django-reversion
    'formtools',  # django-formtools
    'django_filters',  # django-filter
    'corsheaders',
    'rest_framework',
    'bootstrap3',
    'chances_pear', # django-rest-framework
    'apps.projects', #项目管理
    'apps.approvals',  # 飞书管理
    'apps.customers', #客户管理
    'apps.taskms', #任务管理
    'apps.contracts',
    'apps.presales',
    'apps.gpt_service',

]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "chances_pear.middlewares.ThousandSeparatorMiddleware",

]
CORS_ALLOW_ALL_ORIGINS = True
ROOT_URLCONF = "chances_pear.urls"

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = "chances_pear.wsgi.application"


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": "db.sqlite3",
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/
USE_L10N = True
USE_THOUSAND_SEPARATOR = True

LANGUAGE_CODE = 'zh-hans'



# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

# DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
# 静态文件根目录
STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

MEDIA_URL = "/media/"

MEDIA_ROOT = os.path.join(BASE_DIR, "media")

REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': (
        'django_filters.rest_framework.DjangoFilterBackend',
    ),
}

import os

LOGGING_DIR = os.path.join(BASE_DIR, 'logs')  # 创建一个存储日志文件的目录
if not os.path.exists(LOGGING_DIR):
    os.makedirs(LOGGING_DIR)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '{levelname} {asctime} {module} {message}',
            'style': '{',
        },
    },
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': os.path.join(LOGGING_DIR, 'django.log'),  # 日志文件名和路径
            'formatter': 'verbose',
        },
    },
    'root': {
        'handlers': ['file'],
        'level': 'DEBUG',
    },
}

FEISHU_APP_ID = 'cli_9f6864e72bb6d00e'
FEISHU_APP_SECRET = 'mXS0T5R4t4yFUW3kzsxnPJaQBvcjRqi7'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
# OpenAI API key
OPENAI_API_KEY = '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'

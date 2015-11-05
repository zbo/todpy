"""
Django settings for web project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from os.path import abspath, basename, dirname, join, normpath

BASE_DIR = dirname(dirname(abspath(__file__)))
SITE_ROOT = dirname(BASE_DIR)  
SITE_NAME = basename(BASE_DIR)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '5p)21#uatk!^@4^n=nufkii)$0=wwc18k9&k7brz%q%x7yhi=*'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'auto',
    'config',
    'workspace',
    'django_extensions',
    'pipeline',
    'rest_framework'
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'web.urls'

WSGI_APPLICATION = 'web.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = normpath(join(SITE_ROOT, 'static'))
STATICFILES_DIRS = ('./web/static',)

# Configure templates
# TEMPLATES = [  
#     {
#         'BACKEND': 'django.template.backends.django.DjangoTemplates',
#         'DIRS': ['./web/templates'],
#         'APP_DIRS': True,
#         'OPTIONS': {
#             'context_processors': [
#                 'django.template.context_processors.debug',
#                 'django.template.context_processors.request',
#                 'django.contrib.auth.context_processors.auth',
#                 'django.contrib.messages.context_processors.messages',
#             ],
#         },
#     },
# ]

TEMPLATE_DIRS = ('./web/templates',)

# Django Pipeline (and browserify)
STATICFILES_STORAGE = 'pipeline.storage.PipelineCachedStorage'

STATICFILES_FINDERS = (  
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'pipeline.finders.PipelineFinder',
)

# browserify-specific
PIPELINE_COMPILERS = (  
    'pipeline_browserify.compiler.BrowserifyCompiler',
)

PIPELINE_CSS_COMPRESSOR = 'pipeline.compressors.NoopCompressor'  
PIPELINE_JS_COMPRESSOR = 'pipeline.compressors.uglifyjs.UglifyJSCompressor'

if DEBUG:  
    PIPELINE_BROWSERIFY_ARGUMENTS = '-t babelify'

PIPELINE_CSS = {  
    'mysite_css': {
        'source_filenames': (
            'css/style.css',
        ),
        'output_filename': 'css/mysite_css.css',
    },
}

PIPELINE_JS = {  
    'mysite_js': {
        'source_filenames': (
            # 'js/bower_components/jquery/dist/jquery.min.js',
            # 'js/bower_components/react/JSXTransformer.js',
            # 'js/bower_components/react/react-with-addons.js',
            # 'js/app.browserify.js',
        ),
        # 'output_filename': 'js/mysite_js.js',
    }
}

REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ]
}

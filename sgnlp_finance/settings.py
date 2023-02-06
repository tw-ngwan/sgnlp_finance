import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DEBUG = True

# Hostnames that Django site can serve. Security measure to prevent HTTP Host header attacks 
ALLOWED_HOSTS = []

# List of strings representing activated Django applications 
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Add your custom apps here
    'webpack_loader',
    'sgnlp_finance_app', 
]

# List of middleware classes used
# Middleware classes process requests before sending to a view and after a view returns a response.
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Root URL Configuration 
ROOT_URLCONF = 'sgnlp_finance.urls'

# Settings configuring template engine for the project
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

# Loads the React template 
WEBPACK_LOADER = {
    'DEFAULT': {
        'BUNDLE_DIR_NAME': 'static/js',
        'STATS_FILE': os.path.join(BASE_DIR, 'Finance', 'webpack-stats.json'),
    }
}


WSGI_APPLICATION = 'sgnlp_finance.wsgi.application'

# Dictionary setting up db config for project. 
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Password validation rules. Not sure if needed 
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

# Authorized user models 
AUTH_USER_MODEL = 'auth.User'

# Secret key 
SECRET_KEY = '#@2oa3iw-e@zkmlss4_2u3=84mx7)ri$pz&+!249+)%k_k8e@w'

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# URL Path used to serve static files
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
# Directory to link with React files 
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "Finance/build"),
    os.path.join(BASE_DIR, "build"),
]
print(STATICFILES_DIRS)
print(STATIC_ROOT)
for file in os.listdir(STATIC_ROOT):
    print(file)
# if DEBUG:
#     STATICFILES_DIRS = [
#         os.path.join(BASE_DIR, 'static/'),
#     ]


# URL Path used to serve media files. TO BE UPDATED 
MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


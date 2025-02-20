# Minimal Django settings for Next-curl API service
SECRET_KEY = 'your-secret-key'
DEBUG = True
ALLOWED_HOSTS = []
INSTALLED_APPS = [
    'django.contrib.contenttypes',
    'django.contrib.staticfiles',
    # Add your apps here
]
MIDDLEWARE = []
ROOT_URLCONF = 'core.urls'
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'db.sqlite3',
    }
}

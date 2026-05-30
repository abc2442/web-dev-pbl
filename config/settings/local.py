from .base import *  # noqa: F403,F401


ALLOWED_HOSTS = ['danu2442.pythonanywhere.com', 'Danu2442.pythonanywhere.com', 'localhost', '127.0.0.1']
DEBUG = True
STATIC_URL = '/static/'
MEDIA_URL = '/media/'

if os.name == 'nt':
    STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
else:
    STATIC_ROOT = '/home/Danu2442/web-dev-project/static'
    MEDIA_ROOT = '/home/Danu2442/web-dev-project/media'

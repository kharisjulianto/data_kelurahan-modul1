"""
WSGI config for data_keluarahan project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

<<<<<<< HEAD
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'data_keluarahan.settings')
=======
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'data_kelurahan.settings')
>>>>>>> 64461c6 (Initial commit - menambahkan proyek Django data_kelurahan)

application = get_wsgi_application()

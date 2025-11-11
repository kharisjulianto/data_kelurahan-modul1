"""
ASGI config for data_keluarahan project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

<<<<<<< HEAD
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'data_keluarahan.settings')
=======
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'data_kelurahan.settings')
>>>>>>> 64461c6 (Initial commit - menambahkan proyek Django data_kelurahan)

application = get_asgi_application()

import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "secretsanta.settings")

import django

django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()

if not User.objects.filter(username=os.getenv("DJANGO_SUPERUSER_USERNAME")).exists():
    User.objects.create_superuser(
        username=os.getenv("DJANGO_SUPERUSER_USERNAME"),
        email=os.getenv("DJANGO_SUPERUSER_EMAIL"),
        password=os.getenv("DJANGO_SUPERUSER_PASSWORD"),
    )

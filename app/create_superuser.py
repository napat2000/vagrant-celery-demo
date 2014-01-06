import os
import sys
os.environ["DJANGO_SETTINGS_MODULE"] = "celerydemo.settings"

from django.contrib.auth.models import User

user_name, user_email, user_password = sys.argv[1], sys.argv[2], sys.argv[3]
if not User.objects.filter(username=user_name).exists():
    User.objects.create_superuser(user_name, user_email, user_password)
    print "New superuser with username %s created" % user_name
else:
    print "Superuser already exists, skipping..."

from django.test import TestCase
from datetime import timedelta

from django.contrib.auth.hashers import check_password

from models import User

user = User.objects.get(username='admin')
print(check_password(password="12345678", encoded=user.password))
print(user.check_subscription_expiry())

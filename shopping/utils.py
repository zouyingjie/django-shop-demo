# -*- coding: utf-8 -*-
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q

from shopping import models


class CustomBackend(ModelBackend):
    def authenticate(self, username=None, password=None, **kwargs):
        try:
            user = models.User.objects.get(Q(username=username) | Q(user_email=username))
            if user.check_password(password):
                return user
        except Exception as e:
            return None

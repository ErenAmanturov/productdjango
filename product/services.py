from .models import Window
from typing import Type
from .models import User
from django.db.models import QuerySet

class Service:

    @staticmethod
    def fetch_all(model: Type[Window]):
        return (model.objects
                .select_related('user',
                                'profile',
                                'drain',
                                'colour',
                                'reinforce',
                                'slope').all())

    @staticmethod
    def fetch_one(queryset: Type[QuerySet], username, user):
        return (queryset.
                select_related(user).
                only('user__username').
                filter(user__username=username))

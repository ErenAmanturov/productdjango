from .models import Window
from typing import Type
from .models import User


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
    def fetch_one(model: Type[Window], username):
        return (model.objects.
                select_related('user').
                only('user__username').
                filter(user__username=username))

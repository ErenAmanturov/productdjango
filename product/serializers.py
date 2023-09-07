from rest_framework import serializers
from .models import Window
from colorfield.serializers import ColorField


class WindowSerializer(serializers.ModelSerializer):
    # username = serializers.CharField(source='user.username')
    #
    # weight = serializers.IntegerField()
    # height = serializers.IntegerField()
    # profile = serializers.CharField(source='profile.material')
    # colour = serializers.CharField(source='colour.colour')
    # ventilation = serializers.BooleanField()
    # reinforce = serializers.CharField(source='reinforce.reinforce')
    # drain = serializers.CharField(source='drain.drain')
    # slope = serializers.CharField(source='slope.slope')
    # profile_colour = serializers.BooleanField()
    # window = serializers.IntegerField()
    # open_window = serializers.IntegerField()
    # amount = serializers.IntegerField()
    # get_price = serializers.IntegerField()

    class Meta:
        model = Window
        fields = (
            'get_username',
            'weight',
            'height',
            'square',
            'profile',
            'colour',
            'ventilation',
            'reinforce',
            'drain',
            'profile_colour',
            'window',
            'open_window',
            'amount',
            'slope',
            'get_price'
        )


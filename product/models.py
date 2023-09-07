from django.db import models
from user.models import User
from colorfield.fields import ColorField
from uuid import uuid4


class Profile(models.Model):
    # id = models.UUIDField(unique=True, primary_key=True, editable=True, default=uuid4)
    material = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.material


class Colour(models.Model):
    # id = models.UUIDField(unique=True, primary_key=True, editable=True, default=uuid4)
    colour = models.CharField(unique=True, null=True, max_length=100)

    def __str__(self) -> str:
        return self.colour


class Reinforce(models.Model):
    # id = models.UUIDField(unique=True, primary_key=True, editable=True, default=uuid4)
    reinforce = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.reinforce


class Drain(models.Model):
    # id = models.UUIDField(unique=True, primary_key=True, editable=True, default=uuid4)
    drain = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.drain


class Slope(models.Model):
    # id = models.UUIDField(unique=True, primary_key=True, editable=True, default=uuid4)
    slope = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.slope


class Window(models.Model):
    """
    Модель окна

    """
    # id = models.UUIDField(unique=True, primary_key=True, editable=True, default=uuid4)
    weight = models.PositiveSmallIntegerField(default=1)
    height = models.PositiveSmallIntegerField(default=1)
    profile = models.ForeignKey(Profile, on_delete=models.PROTECT, null=True)
    colour = models.ForeignKey(Colour, on_delete=models.PROTECT)
    ventilation = models.BooleanField()
    reinforce = models.ForeignKey(Reinforce, on_delete=models.PROTECT)
    drain = models.ForeignKey(Drain, on_delete=models.PROTECT)
    profile_colour = models.BooleanField()
    window = models.PositiveSmallIntegerField(default=1)
    open_window = models.PositiveSmallIntegerField(default=1)
    amount = models.PositiveIntegerField(default=1)
    slope = models.ForeignKey(Slope, on_delete=models.PROTECT)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Window'
        verbose_name_plural = 'Windows'

    def get_username(self):
        return self.user.username

    # площадь окна

    def square(self):
        square = round((self.height / 1000) * (self.weight / 1000), 2)
        return square

    # Общая цена окон
    def get_price(self):
        price = ((self.square() * 6000) +
                 (500 if self.ventilation else 0) +
                 (1000 if self.profile == 'A' else 500) +
                 (500 if self.reinforce == 'opened 1mm' or self.reinforce == 'closed 1mm' else 1000) * self.amount)
        return round(price)

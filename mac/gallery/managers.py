from datetime import date

from django.db import models


class CurrentExhibitionsManager(models.Manager):
    def get_queryset(self):
        today = date.today()
        return super().get_queryset().filter(start_date__lte=today, end_date__gte=today)


class PastExhibitionsManager(models.Manager):
    def get_queryset(self):
        today = date.today()
        return super().get_queryset().filter(end_date__lt=today)


class FutureExhibitionsManager(models.Manager):
    def get_queryset(self):
        today = date.today()
        return super().get_queryset().filter(start_date__gt=today)

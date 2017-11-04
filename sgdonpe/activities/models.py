import json

from django.db.models.functions import TruncMonth, TruncDay
from django.db.models import Count

from django.contrib.auth.models import User
from django.db import models

class Activity(models.Model):
    FIRMAR = 'F'
    VISAR = 'V'
    ENVIAR = 'E'
    LEER = 'L'
    ACTIVITY_TYPES = (
        (FIRMAR, 'Firmar'),
        (VISAR, 'Visar'),
        (ENVIAR, 'Enviar'),
        (LEER, 'Leer'),
        )

    user = models.ForeignKey(User)
    activity_type = models.CharField(max_length=1, choices=ACTIVITY_TYPES)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Activity'
        verbose_name_plural = 'Activities'

    @staticmethod
    def monthly_activity(user):
        """Static method to retrieve monthly statistical information about the
        user activity.
        @requires:  user - Instance from the User Django model.
        @returns:   Two JSON arrays, the first one is dates which contains all
                    the dates with activity records, and the second one is
                    datapoints containing the sum of all the activity than had
                    place in every single month.

        Both arrays keep the same order, so there is no need to order them.
        """
        # months = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
        # "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
        query = Activity.objects.filter(user=user).annotate(
            month=TruncMonth('date')).values('month').annotate(
                c=Count('id')).values('month', 'c')
        try:
            dates, datapoints = zip(
                *[[a['c'], str(a['month'].date())] for a in query])
            return json.dumps(dates), json.dumps(datapoints)

        except ValueError:
            return json.dumps(0), json.dumps(0)

    @staticmethod
    def daily_activity(user):
        """Static method to retrieve daily statistical information about the
        user activity.
        @requires:  user - Instance from the User Django model.
        @returns:   Two JSON arrays, the first one is dates which contains all
                    the dates with activity records, and the second one is
                    datapoints containing the sum of all the activity than had
                    place in every single day.

        Both arrays keep the same order, so there is no need to order them.
        """
        query = Activity.objects.filter(user=user).annotate(day=TruncDay(
            'date')).values('day').annotate(c=Count('id')).values('day', 'c')
        try:
            dates, datapoints = zip(
                *[[a['c'], str(a['day'].date())] for a in query])
            return json.dumps(dates), json.dumps(datapoints)

        except ValueError:
            return json.dumps(0), json.dumps(0)

    def __str__(self):
        return self.activity_type


from __future__ import unicode_literals

from django.db import models
from geoposition.fields import GeopositionField

class Country(models.Model):
	name = models.CharField(max_length=100, null=False, blank=False)

	def __unicode__(self):
		return self.name


class PointOfInterest(models.Model):
	name = models.CharField(max_length=50)
	address = models.CharField(max_length=100)
	position = GeopositionField()
	country = models.ForeignKey(Country, blank=True, null=True)

	def __unicode__(self):
		return self.name
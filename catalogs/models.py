from django.db import models

from django.contrib.postgres.fields import ArrayField


class Catalog(models.Model):
	title = models.CharField(max_length=100, help_text='A title for your dataset.')
	description = models.CharField(max_length=500, help_text='Give a brief description of your data.')
	creation_date = models.DateTimeField('creation date', help_text='The date in which your data was created')
	creators = ArrayField(models.CharField(max_length=35, blank=True), size=10, help_text='If it is more than one, separate by commas')
	subjects = ArrayField(models.CharField(max_length=35, blank=True), size=5, help_text='If it is more than one, separate by commas')
	instrument = models.CharField(max_length=50, help_text='Name of the instrument that produced the data')
	facility = models.CharField(max_length=50, help_text='Name of the facility at which data was taken')

	ARCHIVE = 'AR'
	BIBLIOGRAPHY = 'BI'
	CATALOG = 'CA'
	JOURNAL = 'JO'

	TYPES_CHOICES = (
		(ARCHIVE, 'Archive'),
		(BIBLIOGRAPHY, 'Bibliography'),
		(CATALOG, 'Catalog'),
		(JOURNAL, 'Journal'),
	)

	type = models.CharField(
		max_length=2,
		choices=TYPES_CHOICES,
		default=CATALOG,
		help_text='Choose the classification that best fits your data.'
	)

	coverage_profile = models.CharField(max_length=200, help_text='Specify the space-time coordinates (STC) according to the IVOA STC data model.')

	ONE_OF_RADIO = 'OR'
	OPTICAL = 'OP'
	UV = 'UV'

	COVERAGE_WAVEBANDS_CHOICES = (
		(ONE_OF_RADIO, 'One of Radio'),
		(OPTICAL, 'Optical'),
		(UV, 'UV'),
	)

	coverage_waveband = models.CharField(
		max_length=2,
		choices=COVERAGE_WAVEBANDS_CHOICES,
		default=ONE_OF_RADIO,
		help_text='Choose the classification that best fits your data.'
	)
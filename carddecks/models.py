from django.db import models
from users.models import *
from django.utils.text import slugify

# Create your models here.
class Deck(models.Model):
	user = models.CharField(max_length = 30)
	name = models.CharField(max_length = 30)
	slug = models.SlugField(unique = True, blank = True, null = True)

	def save(self, *args, **kwargs):
		self.slug = slugify(self.name)
		super(Deck, self).save(*args, **kwargs)

	class Meta:
		verbose_name = 'Deck'
		verbose_name_plural = 'Decks'

	def __str__(self):
		return self.name


class Card(models.Model):
	user = models.CharField(max_length = 30)
	deck_name = models.CharField(max_length = 30)
	front = models.TextField(max_length = 100)
	back = models.TextField(max_length = 100)

	class Meta:
		verbose_name = 'Card'
		verbose_name_plural = 'Cards'

	def __str__(self):
		return self.front
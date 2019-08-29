from django.db import models

# Create your models here.

class User(models.Model):
	email = models.CharField(max_length = 30)
	password = models.CharField(max_length = 30)
	is_active = models.IntegerField(blank = True, null = True)
	activation_code = models.CharField(max_length = 20, blank = True, null = True)

	class Meta:
		verbose_name = 'User'
		verbose_name_plural = 'Users'

	def __str__(self):
		return self.email
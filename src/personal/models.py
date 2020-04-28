from django.db import models

# Create your models here.
PRIORITY = [
	("L","Low"),
	("M","Medium"),
	("H","High")
]

class Question(models.Model):
	title					= models.CharField(max_length = 60)
	question  				= models.TextField(max_length = 400)
	priority  				= models.CharField(max_length = 1,choices = PRIORITY)

	def __str__(self):
		return self.title

	class Meta:
		verbose_name = 'Quesiton' 
		verbose_name_plural = "All Questions"
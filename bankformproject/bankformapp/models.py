from django.db import models

# Create your models here.
class Bankform(models.Model):
	FIRSTNAME = models.CharField(max_length=50)
	LASTNAME = models.CharField(max_length=50)
	ADDRESS = models.CharField(max_length=50)
	AGE = models.IntegerField()
	DOB = models.DateField()
	BRANCH = models.CharField(max_length=50)
	PHONENO = models.IntegerField()
	EMAIL = models.EmailField()
	class Meta:
		verbose_name = "Bankform"
		verbose_name_plural = "Bankforms"
		def __str__(self):
			pass


from django.db import models

# Create your models here.
class trainer_info(models.Model):
	FIRSTNAME = models.CharField(max_length=50)
	LASTNAME = models.CharField(max_length=50)
	DOMAIN = models.CharField(max_length=50)
	BRANCH = models.CharField(max_length=50)
	
	ADDRESS = models.CharField(max_length=50)
	EXPERIENCE = models.IntegerField()
	SALARY = models.IntegerField()
	class Meta:
		verbose_name = "trainer_info"
		verbose_name_plural = "trainer_infos"
		def __str__(self):
			pass


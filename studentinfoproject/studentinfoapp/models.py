from django.db import models

# Create your models here.
class student_info(models.Model):
	FIRSTNAME = models.CharField(max_length=50)
	LASTNAME = models.CharField(max_length=50)
	CLG = models.CharField(max_length=50)
	BRANCH = models.CharField(max_length=50)
	CGPA = models.IntegerField()
	class Meta:
		verbose_name = "student_info"
		verbose_name_plural = "student_infos"
		def __str__(self):
			pass


from django.db import models


class Entry(models.Model):
	diary_id = models.AutoField(primary_key=True)
	date = models.DateField()
	text = models.TextField(max_length=300)

	def __str__(self):
		return self.name


from django.db import models

# Create your models here.

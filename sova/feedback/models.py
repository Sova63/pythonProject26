from django.db import models
from domain.models import User



'''class Entry(models.Model):
	user_id = models.ForeignKey(User, on_delete=models.CASCADE)
	username = models.ForeignKey(User, on_delete=models.CASCADE)
	diary_id = models.AutoField(primary_key=True)
	date = models.DateField()
	text = models.TextField(max_length=300)'''

class Entry(models.Model):
	user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='entries_by_user')
	username = models.ForeignKey(User, on_delete=models.CASCADE, related_name='entries_by_username')
	diary_id = models.AutoField(primary_key=True)
	date = models.DateField()
	text = models.TextField(max_length=300)

	def __str__(self):
		return self.name




from django.db import models

# Create your models here.

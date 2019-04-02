from django.db					import models
from django.contrib.auth.models	import User

class HighScore(models.Model):
	user = models.OneToOneField(User, on_delete = models.CASCADE)
	score = models.IntegerField(default = 0)

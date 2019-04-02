from django.db					import models
from django.contrib.auth.models	import User

class CurrentGame(models.Model):
	user = models.OneToOneField(User, on_delete = models.CASCADE)
	search_term = models.TextField()

class HighScore(models.Model):
	user = models.OneToOneField(User, on_delete = models.CASCADE)
	score = models.IntegerField(default = 0)

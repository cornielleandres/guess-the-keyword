from django.db					import models
from api.models					import CustomUser

class CurrentGame(models.Model):
	user = models.OneToOneField(CustomUser, on_delete = models.CASCADE)
	search_term = models.TextField()

class HighScore(models.Model):
	user = models.OneToOneField(CustomUser, on_delete = models.CASCADE)
	score = models.IntegerField(default = 0)

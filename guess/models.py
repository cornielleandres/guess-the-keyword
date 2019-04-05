from django.db					import models
from api.models					import CustomUser

class CurrentGame(models.Model):
	user = models.OneToOneField(CustomUser, on_delete = models.CASCADE)
	search_term = models.TextField()
	points = models.IntegerField(default = 0)
	strikes = models.IntegerField(default = 0)

class HighScore(models.Model):
	user = models.ForeignKey(CustomUser, on_delete = models.CASCADE)
	points = models.IntegerField(default = 0)

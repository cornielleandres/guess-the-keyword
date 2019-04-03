from django.contrib	import admin
from .models		import CurrentGame, HighScore

admin.site.register(CurrentGame)
admin.site.register(HighScore)

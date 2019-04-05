from django.shortcuts	import render, redirect
from decouple			import config
import requests

from .models			import CurrentGame, HighScore
from .utils				import get_random_word

def index(request):
	user = request.user
	if not user.is_authenticated:
		return redirect('account_login')
	message = 'Guess what the keyword is.'
	try: # see if a current game exists for this user
		current_game = CurrentGame.objects.get(user_id = user.id)
	except CurrentGame.DoesNotExist: # if current game does not exist for this user
		search_term = get_random_word()
		CurrentGame.objects.create(user = user, search_term = search_term)
		current_game = CurrentGame.objects.get(user_id = user.id)
	else: # else if current game exists for this user
		if request.method == 'POST': # if a post request was made, they took a guess
			guess = request.POST.get('guess', False).lower().strip()
			current_search_term = current_game.search_term
			if guess == current_search_term: # if user guessed correctly
				current_game.points = current_game.points + 1
				current_game.search_term = get_random_word()
				current_game.save()
				message = 'CORRECT! The keyword was {}!'.format(guess)
			else: # else if user guessed wrong
				current_game.strikes = current_game.strikes + 1
				current_game.search_term = get_random_word()
				current_game.save()
				message = 'Nope. It\'s not {}.'.format(guess)
				if current_game.strikes >= 3: # if user made 3 wrong guesses
					high_scores = HighScore.objects.all().order_by('points')
					lowest_high_score = high_scores[0]
					# if user got equal or more points than the lowest high score
					if lowest_high_score.points <= current_game.points:
						if len(high_scores) >= 3: # if there are already 3 high scores
							lowest_high_score.delete()
						HighScore.objects.create(user = user, points = current_game.points)
						message = 'Game over! You got a high score!'
					else: # else if user did not get a high score
						message = 'Game over!'
					current_game = CurrentGame.objects.get(user_id = user.id)
					current_game.delete()
					context = {
						'current_search_term': current_search_term,
						'message': message,
						'points': current_game.points,
						'high_scores': HighScore.objects.all().order_by('-points'),
					}
					return render(request, 'guess/game-over.html', context)
		search_term = current_game.search_term
	pixabay_key = config('PIXABAY_KEY')
	image_type = 'vector'
	url = (
		'https://pixabay.com/api/?'
		'key=' + pixabay_key +
		'&q=' + search_term +
		'&image_type=' + image_type
	)
	response = requests.get(url)
	results = response.json()
	try:
		# get top 10 images
		images = [ hit['webformatURL'] for i, hit in enumerate(results['hits']) if i < 10 ]
	except:
		error = results['error']
		context = { 'error': error }
		return render(request, 'guess/error.html', context)
	word_clue = [ '_' for i in range(len(search_term)) ]
	word_clue[0] = search_term[0]
	context = {
		'images': images,
		'message': message,
		'points': current_game.points,
		'word_clue': word_clue,
		'strikes': current_game.strikes,
		'user': user,
	}
	return render(request, 'guess/index.html', context)

from django.shortcuts	import render, redirect
from decouple			import config
import requests

from .models			import CurrentGame
from .utils				import get_random_word

def index(request):
	user = request.user
	if not user.is_authenticated:
		return redirect('api:login')
	try:
		current_game = CurrentGame.objects.get(user_id = user.id)
		method = request.POST.get('_method', '')
		if method == 'put':
			current_game.delete()
			search_term = get_random_word()
			CurrentGame.objects.create(user = user, search_term = search_term)
		else:
			search_term = current_game.search_term
	except CurrentGame.DoesNotExist:
		search_term = get_random_word()
		CurrentGame.objects.create(user = user, search_term = search_term)
	api_key = config('GOOGLE_API_KEY')
	google_cs_id = config('GOOGLE_CS_ID')
	request_url = (
		'https://www.googleapis.com/customsearch/v1?'
		'q=' + search_term +
		'&cx=' + google_cs_id +
		'&exactTerms=' + search_term +
		'&imgSize=medium'
		'&searchType=image'
		'&safe=active'
		'&key=' + api_key
	)
	response = requests.get(request_url)
	results = response.json()
	try:
		images = [ image['link'] for image in results['items'] ]
	except:
		error = results['error']
		return render(request, 'guess/error.html', { 'error': error })
	context = {
		'images': images,
		'search_term': search_term,
		'user': user,
	}
	if request.method == 'POST':
		guess = request.POST.get('guess', False)
		context['guess'] = guess
	return render(request, 'guess/index.html', context)

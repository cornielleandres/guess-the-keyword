from django.shortcuts	import render
from decouple			import config
import requests

def index(request):
	api_key = config('GOOGLE_API_KEY')
	google_cs_id = config('GOOGLE_CS_ID')
	search_term = 'house'
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
	user = request.user
	results = response.json()
	print(results)
	images = [ image['link'] for image in results['items'] ]
	context = {
		'user': user,
		'images': images,
	}
	return render(request, 'guess/index.html', context)

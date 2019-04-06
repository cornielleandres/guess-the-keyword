from .base	import *

DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS.append('whitenoise.runserver_nostatic')

DATABASES = {
	'default': {
		'ENGINE': config('ENGINE'),
		'NAME': config('DATABASE'),
		'USER': config('USER'),
		'PASSWORD': config('PASSWORD'),
		'HOST': config('HOST'),
		'PORT': '',
	}
}

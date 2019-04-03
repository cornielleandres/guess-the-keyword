from .base	import *

DEBUG = True

ALLOWED_HOSTS = []

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

from django.urls		import include, path
from django.conf.urls	import url
from .					import views

app_name = 'api'
urlpatterns = [
	path('accounts/', include('django.contrib.auth.urls'), name = 'login'),
	path('accounts/register/', views.Register.as_view(), name = 'register'),
]

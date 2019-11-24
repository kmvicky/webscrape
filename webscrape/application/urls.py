import application.views as views

from django.urls import include, path, re_path

app_name = 'application'

urlpatterns = [
	
	path('',
		views.NiftyGainers.as_view({
			'get':'list',
		}),
		name='niftygainers'),

	path('niftygainers',
		views.NiftyGainers.as_view({
			'get':'retrieve',
		}),
		name='getniftygainers'),
]
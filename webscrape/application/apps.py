from django.apps import AppConfig

class ApplicationConfig(AppConfig):

	name = 'webscrape.application'
	verbose_name = 'application'

	def ready(self):
		pass